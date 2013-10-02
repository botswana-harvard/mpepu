from bhp_actg_reference.models import Appendix40
from edc.subject.code_lists.models import DxCode


def ImportCode(**kwargs):
    
    """import dx codes for this protocol. run bhp_actg_reference.utils.ImportAppendix() first"""

    appendix40 = Appendix40.objects.all()
    for app40 in appendix40:
        if not DxCode.objects.filter(code=app40.code):
            DxCode.objects.create(
                code = app40.code[0:15],
                short_name = app40.short_description[0:35],
                long_name = app40.full_description[0:255],
                list_ref = 'actg_app40'
                )
            print app40.code

