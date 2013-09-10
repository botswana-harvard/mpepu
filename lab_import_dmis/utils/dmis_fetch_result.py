import sys,os
from datetime import datetime, timedelta
sys.path.append('/home/django/source/')
sys.path.append('/home/django/source/bhplab/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bhplab.settings'
from django.core.management import setup_environ
from bhplab import settings

setup_environ(settings)

import pyodbc, re
from lab_result.models import ResultSource
from django.db.models import Avg, Max, Min, Count        
from lab_receive.models import Receive
from lab_aliquot.models import Aliquot
from lab_aliquot_list.models import AliquotType, AliquotCondition,AliquotMedium
from lab_order.models import Order
from lab_result.models import Result, ResultSource
from lab_result_item.models import ResultItem
from lab_panel.models import Panel, PanelGroup, TidPanelMapping
from lab_patient.models import Patient
from lab_account.models import Account
from bhp_research_protocol.models import Protocol, PrincipalInvestigator, SiteLeader, FundingSource
from lab_common.utils import AllocateResultIdentifier
from lab_test_code.models import TestCode, TestCodeGroup


"""
import results for orders already in the system
"""

def fetch_results_from_dmis(**kwargs):
    subject_identifier = kwargs.get('subject_identifier')
    days = kwargs.get("days")
    import_tdelta = 90
    if days:
        try:
            import_tdelta = int(days)
        except:
            import_tdelta = 90

    if subject_identifier:
        print subject_identifier
        orders  = Order.objects.filter(aliquot__receive__patient__subject_identifier__icontains=subject_identifier)    
        order_count = orders.count()        
    #elif:
    #    orders  = Order.objects.filter(imported=imported)        
    elif import_tdelta:
        now  = datetime.today()
        import_datetime_cutoff = now - timedelta(days=import_tdelta) 
        order_pks = Result.objects.values('order__pk').filter(order__modified__lte=import_datetime_cutoff)
        orders = Order.objects.exclude(pk__in=order_pks).order_by('-created')
        order_count = orders.count()        
    else:
        orders  = Order.objects.all().order_by('-created')
        order_count = orders.count()
    
    tot = order_count
    for order in orders:
        create_or_update_result(order=order)
        order_count -= 1
        print '%s %s/%s' % (order.order_identifier, order_count, tot)

def create_or_update_result(**kwargs):

    order = kwargs.get('order')
        
    cnxn2 = pyodbc.connect("DRIVER={FreeTDS};SERVER=192.168.1.141;UID=sa;PWD=cc3721b;DATABASE=BHPLAB")
    cursor_result = cnxn2.cursor()

    cnxn3 = pyodbc.connect("DRIVER={FreeTDS};SERVER=192.168.1.141;UID=sa;PWD=cc3721b;DATABASE=BHPLAB")
    cursor_resultitem = cnxn3.cursor()
    result = None
    if Result.objects.filter(order=order):
        # get the existing result
        result = Result.objects.filter(order=order)
        if result.count()>1:
            # get rid of duplicates
            print '....duplicates found for %s' % (result[0].result_identifier,)
            dups = Result.objects.filter(order=order).exclude(pk=result[0].pk)
            for dup in dups:
                ritems = ResultItem.objects.filter(result=dup)
                for ri in ritems:
                    ri.delete()
                dup.delete()            
                print '........deleted'
        result = Result.objects.get(order=order)
        print 'Result exists (%s)' % (result.result_identifier,)
    else:
        # create new result        
        # fetch the order/result from DMIS (note in DMIS orders are generated when a result is available so orders always have results)
        sql ='select distinct headerdate as result_datetime, \
              l21.keyopcreated as user_created, \
              l21.datecreated as created, \
              convert(varchar(36), l21.result_guid) as result_guid \
              from BHPLAB.DBO.LAB21Response as L21 \
              left join BHPLAB.DBO.LAB21ResponseQ001X0 as L21D on L21.Q001X0=L21D.QID1X0 \
              where l21.id=\'%s\' and l21d.id is not null'  % order.order_identifier
        cursor_result.execute(sql) # should return 0 or 1 row because l21.id is a primary key
        for row in cursor_result:
            # allocate a result identifier for this new result
            result_identifier=AllocateResultIdentifier(order)    
            # create the result record
            result = Result.objects.create(
                result_identifier=result_identifier,
                order = order,
                result_datetime=row.result_datetime,
                comment='',
                user_created=row.user_created,
                created=row.created,
                dmis_result_guid=row.result_guid,
                )
                
            print 'created order %s %s result %s' % ( order.order_identifier, order.order_datetime, result.result_identifier)
        fetch_or_create_resultsource()
        
    # create or update the result items for this result
    if result:
        # get list of result items for this result from DMIS (LAB21ResponseQ001X0)
        sql ='select l21d.sample_assay_date, \
              utestid as code, \
              result as result_value, \
              result_quantifier, \
              status, \
              mid,\
              l21d.validation_ref as validation_reference, \
              l21d.datelastmodified as result_item_datetime, \
              l21d.keyopcreated as user_created, \
              l21d.keyoplastmodified as user_modified, \
              l21.datecreated as created, \
              l21.datelastmodified as modified \
              from BHPLAB.DBO.LAB21Response as L21 \
              left join BHPLAB.DBO.LAB21ResponseQ001X0 as L21D on L21.Q001X0=L21D.QID1X0 \
              where l21.id=\'%s\' and l21d.id is not null'  % result.order.order_identifier
        
        cursor_resultitem.execute(sql)
        # loop thru result items
        for ritem in cursor_resultitem:
            create_or_update_resultitem(result=result, ritem=ritem)                

    return None
    
def create_or_update_resultitem(**kwargs):

    result = kwargs.get('result')
    ritem = kwargs.get('ritem')    
    code = ritem.code.strip(' \t\n\r')
    if ResultItem.objects.filter(result=result, test_code__code=code):
        # update
        user = get_ritem_user(ritem.user_modified)            
        validation = get_ritem_validation(ritem)
        for result_item in ResultItem.objects.filter(result=result, test_code__code=code).exclude(modified__gt=ritem.modified):
            result_item.result_item_datetime=ritem.result_item_datetime
            result_item.result_item_value=ritem.result_value
            result_item.result_item_quantifier=ritem.result_quantifier
            result_item.validation_status='P'
            result_item.validation_reference=validation['validation_reference']
            result_item.result_item_source=validation['result_item_source']
            result_item.result_item_source_reference=validation['result_item_source_reference']
            result_item.result_item_operator=user                
            comment=''
            result_item.save()
            print '----updated %s modified on %s' % (code, ritem.modified)
    else:
        # create
        test_code = fetch_or_create_testcode(code)
        user = get_ritem_user(ritem.user_created)            
        validation = get_ritem_validation(ritem)
        # create a new result item. set validation to 'P', we'll import 
        # full validation information later 
        ResultItem.objects.create(
            result=result,
            test_code=test_code,
            result_item_datetime=ritem.result_item_datetime,                
            result_item_value=ritem.result_value,
            result_item_quantifier=ritem.result_quantifier,
            validation_status='P',
            validation_reference=validation['validation_reference'],
            result_item_source=validation['result_item_source'],
            result_item_source_reference=validation['result_item_source_reference'],
            result_item_operator=user,                
            comment='',
            )
        print '----added %s' % (code)        
        
def get_ritem_user(dmis_user):
    # change NT system username to auto
    if dmis_user.strip(' \t\n\r').upper() == 'NT AUTHORITY\SYSTEM':
        user = 'auto'
    else:
        user = dmis_user    
    return user
    
def get_ritem_validation(ritem):

    result_item_source = ''
    result_item_source_reference = ''
    validation_reference = ''
    
    # evaluate validation_reference
    if ritem.validation_reference == '-9':
        # this is an item from GetResults TCP connected to PSM
        result_item_source = fetch_or_create_resultsource(interface='psm_interface')                
        result_item_source_reference = ''
        validation_reference = 'dmis-auto'
    elif ritem.validation_reference == 'LAB21:MANUAL':
        # manual entry and no validation -- straight to LAB21 tableset
        result_item_source = fetch_or_create_resultsource(interface='manual_entry')                
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'auto'                
    elif re.search('^rad[0-9A-F]{5}\.tmp$', ritem.validation_reference):    
        # this is an item from GetResults Flatfile and validated via the LAB05 path
        result_item_source = fetch_or_create_resultsource(interface='cd4_interface')
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'lab05'                               
    elif re.search('^LAB23:', ritem.validation_reference):          
        # manual entry and validated via the LAB23 validation path                           
        result_item_source = fetch_or_create_resultsource(interface='manual_entry')
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'lab23'                               
    elif re.search('^IMPORT', ritem.validation_reference):          
        # manual entry and validated via the LAB23 validation path                           
        result_item_source = fetch_or_create_resultsource(interface='direct_import')
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'auto'     
    elif re.search('^LB003:', ritem.validation_reference):          
        # manual import                           
        result_item_source = fetch_or_create_resultsource(interface='direct_import')
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'auto'     
    elif re.search('^LB004:', ritem.validation_reference):          
        # manual import                           
        result_item_source = fetch_or_create_resultsource(interface='direct_import')
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'auto'  
    elif re.search('^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$', ritem.validation_reference):                   
        # manual import                                           
        result_item_source = fetch_or_create_resultsource(interface='manual_entry')
        result_item_source_reference = 'dmis-%s' % ritem.validation_reference
        validation_reference = 'auto'  
    else:
        # missed a case? let's hear about it
        raise TypeError('Validation reference \'%s\' was not expected. See dmis_fetch_result.' % ritem.validation_reference)

    result_item_source_reference = '%s %s' % (result_item_source_reference, ritem.mid)

    return {'validation_reference': validation_reference, 'result_item_source':result_item_source,'result_item_source_reference':result_item_source_reference}


def fetch_or_create_resultsource( **kwargs ):

    interfaces = ['psm_interface', 'cd4_interface','auto', 'manual_entry', 'direct_import',]
    agg = ResultSource.objects.aggregate(Max('display_index'),)
    if agg:
        display_index = agg['display_index__max']
    else:
        display_index = 0    

    # populate if not already ...
    for interface in interfaces:
        if not ResultSource.objects.filter(name__iexact=interface):
            result_source=ResultSource.objects.create(
                name=interface,
                short_name=interface,                
                display_index=display_index+10,
                )
            result_source.save()  
    # create a new one if given argument and does not exist already
    if kwargs.get('interface'):        
        if not ResultSource.objects.filter(name__iexact=kwargs.get('interface')):
            result_source=ResultSource.objects.create(
                name=kwargs.get('interface'),
                short_name=kwargs.get('interface'),                
                display_index=display_index+11,
                )
            result_source.save()  
        else:
            result_source=ResultSource.objects.get(name__iexact=kwargs.get('interface'))                        
    else:
        result_source = None
            
    return result_source         

def fetch_or_create_testcode(code):
    try:
        test_code = TestCode.objects.get(code__exact=code)
    except:
        test_code_group = TestCodeGroup.objects.get(code__exact='000')
        TestCode.objects.create( 
            code=code,
            name=code,
            units='-',
            test_code_group=test_code_group,
            display_decimal_places=0,  
            is_absolute='absolute',
            )  
        test_code = TestCode.objects.get(code__iexact=code)                           
    return test_code

if __name__ == "__main__":
    print 'fetching lab results from dmis....'
    if len(sys.argv) > 1:
        fetch_results_from_dmis(subject_identifier=sys.argv[1])
    else:
        fetch_results_from_dmis()
    print 'Done'
    sys.exit (0)                  
