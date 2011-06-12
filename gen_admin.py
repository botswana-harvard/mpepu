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

def gen_admin( **kwargs):
    
    """generate text for admin.py given a list of models and a base model"""
    
    from string import Template
    from django.contrib.contenttypes.models import ContentType

    app_label = kwargs.get("app_label", 'mpepu_maternal')
    foreign_key_field = kwargs.get("foreign_key", "maternal_visit")
    base_model_admin = kwargs.get("base", 'MyMaternalVisitModelAdmin')

    #app_label = 'mpepu_maternal'
    #foreign_key_field = "registered_subject"
    #base_model_admin = 'MyRegisteredSubjectModelAdmin'

    #app_label = 'mpepu_infant'
    #foreign_key_field = "infant_visit"
    #base_model_admin = 'MyInfantVisitModelAdmin'

    app_label = 'mpepu_infant'
    foreign_key_field = "registered_subject"
    base_model_admin = 'MyRegisteredInfantModelAdmin'

    s = Template("\n# ${model}\n\
class ${model}Admin(${base}): \n\
\n\
    form = ${model}Form\n\
\n\
    fields = (\n        ${fields}\n    )\n\
\n\
    radio_fields = {\n        ${radio_fields}\n    }\n\
\n\
    filter_horizontal = (\n        ${filter_horizontal}\n    )\n\
\n\
    \"\"\"${related}\"\"\"\n\
\n\
admin.site.register(${model}, ${model}Admin)")

    model_names = []
    contenttypes = ContentType.objects.all()
    [model_names.append(ctype.model) for ctype in ContentType.objects.filter(app_label=app_label)]

    # get model class from content type
    for model_name in model_names:
        model = ContentType.objects.get(model=model_name).model_class()
        object_name = model._meta.__dict__['object_name']
        for field in model._meta.fields:
            if field.name == foreign_key_field:
                # list fields        
                fields = [] 
                choice_fields = [] 
                related = []  
                for field in model._meta.fields:
                    if field.name not in ['created', 'modified', 'user_created', 'user_modified', 'hostname_created', 'hostname_modified', 'id',]:
                        fields.append('"'+field.name+'"')
                    # if field has choices, add to choice_fields            
                    if not field.__dict__['_choices'] == []:
                       choice_fields.append('"%s":admin.VERTICAL' % field.name)
                    try:
                        if field.__dict__['related']:
                            related.append(field.__dict__['related'].__dict__['parent_model']._meta.module_name)
                    except:
                        pass        
                # if field has manytomany add to filter_horizontal
                m2m_fields = []            
                [m2m_fields.append('"'+f.name+'"') for f in model._meta.many_to_many]

                print s.substitute(
                    model = object_name,
                    base = base_model_admin, 
                    fields = ',\n        '.join(fields),        
                    radio_fields = ',\n        '.join(choice_fields),        
                    filter_horizontal = ',\n        '.join(m2m_fields),
                    related = ', '.join(related),
                    )

def gen_form( **kwargs):

    """generate text for forms.py"""

    from string import Template

    model=kwargs.get("model")
    base_model_admin=kwargs.get("base")
    
    s = Template("# ${model}\n\
class ${model}Form (${base}): \n\
    def clean(self):\n\
    \n\
    cleaned_data = self.cleaned_data \n\
    \n\
    return cleaned_data\n\
        \n\
    class Meta:\n\
        model = ${model}")

    print s.substitute(model=model, base=base_model_admin)


gen_admin()


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
