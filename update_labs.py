#!/usr/bin/env python
import sys, os

def main(argv):
    
    if len(argv) > 1:
        subject_identifier=argv[1]
    else:
        subject_identifier=None
        
    if subject_identifier:
        registered_subjects = RegisteredSubject.objects.filter(subject_identifier=subject_identifier).order_by('subject_identifier')
    else:    
        registered_subjects = RegisteredSubject.objects.all()
    total = registered_subjects.count()
    cnt = 0
    dmis = Dmis()
    dmis_receive = DmisReceive()
    dmis_order = DmisOrder()

    for registered_subject in registered_subjects:
        
        subject_identifier = registered_subject.subject_identifier

        dmis.fetch(subject_identifier=subject_identifier, lab_db='lab_api')
        dmis_receive.fetch(subject_identifier=subject_identifier, lab_db='lab_api')
        dmis_order.fetch(subject_identifier=subject_identifier, lab_db='lab_api')
        
        cnt += 1
        if Lab.objects.filter(subject_identifier=subject_identifier, result__isnull=True):
            Lab.objects.filter(subject_identifier=subject_identifier, result__isnull=True).delete()
        labs = Lab.objects.fetch(subject_identifier=subject_identifier)
        
        if labs:
            results = Result.objects.fetch(subject_identifier=subject_identifier, labs=labs)
            if results:
                ResultItem.objects.fetch(subject_identifier=subject_identifier, results=results)
        print '%s %s/%s' % (subject_identifier, cnt, total)

if __name__=="__main__":

    #import sys, os
    sys.path.append('/home/django/source/bhp056/')
    os.environ['DJANGO_SETTINGS_MODULE'] ='bhp056.settings'
    try:
        import settings
    except ImportError:
        import sys
        sys.stderr.write("Couldn't find the settings.py module.")
        sys.exit(1)
    from django.core.management import setup_environ
    setup_environ(settings)
    from bhp_registration.models import RegisteredSubject
    from lab_clinic_api.models import Lab, Result, ResultItem
    from lab_import_dmis.classes import Dmis, DmisReceive, DmisOrder
    main(sys.argv[1:])
