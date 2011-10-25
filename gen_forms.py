#!/usr/bin/env python
import re
from django.core.management import setup_environ

try:
    import settings
except ImportError:
    import sys
    sys.stderr.write("Couldn't find the settings.py module.")
    sys.exit(1)

setup_environ(settings)


def gen_form( **kwargs):

    """generate text for forms.py"""

    from string import Template
    from django.contrib.contenttypes.models import ContentType

    s = Template("# ${model}\n\
class ${model}Form (${base}): \n\
    def clean(self):\n\
    \n\
        cleaned_data = self.cleaned_data \n\
    \n\
        return cleaned_data\n\
        \n\
    class Meta:\n\
        model = ${model}\n\n")

    app_label = kwargs.get("app_label", 'lab_barcode')
    #foreign_key_field = kwargs.get("foreign_key", "visit")
    base_model_admin = kwargs.get("base", 'MaternalVisitModelAdmin')
    model_names = []
    object_names = []
    contenttypes = ContentType.objects.all()
    [model_names.append(ctype.model) for ctype in ContentType.objects.filter(app_label=app_label)]

    # get model class from content type
    
    for model_name in model_names:
        model = ContentType.objects.get(model=model_name).model_class()
        object_names.append(model._meta.__dict__['object_name'])

    print 'from django import forms\nfrom django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer\nfrom bhp_common.classes import MyModelForm'
    print 'from {app_label}.models import '.format(app_label=app_label) + ', '.join(object_names)+'\n\n\n'
            
    for object_name in object_names:
        print s.substitute(model=object_name, base='MyModelForm')


gen_form()


"""
if __name__ == "__main__":

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-m", "--model", dest="model_name",
                      help="model name", metavar="MODEL_NAME")
    parser.add_option("-b", "--base", dest="base_model_name",
                      help="base model name", metavar="BASE_MODEL_NAME")
    (options, args) = parser.parse_args()


    print '"""" admin """"'        
    for m in models:
        gen_admin( model=m, base='MyModelAdmin', )
        
        
    print '"""" forms """"'        
    for m in models:
        gen_form( model=m, base='forms.ModelForm', )        
"""
