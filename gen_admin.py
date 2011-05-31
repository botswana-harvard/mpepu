
def gen_admin( **kwargs):
    from string import Template

    model=kwargs.get("model")
    base=kwargs.get("base")

    s = Template("# ${model}\n\
class ${model}Admin($base}): \n\
\n\
    form = ${model}Form\n\
\n\
    def save_model(self, request, obj, form, change):\n\
        if change:\n\
            obj.user_modified = request.user\n\
            obj.save()\n\
        if not change:\n\
            obj.user_created = request.user\n\
            obj.save()\n\
\n\
admin.site.register(${model}, ${model}Admin)")

    print s.substitute(model=model,base=base)

def gen_form( **kwargs):
    from string import Template

    model=kwargs.get("model")
    base=kwargs.get("base")
    
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

    print s.substitute(model=model, base=base)

if __name__ == "__main__":

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-m", "--model", dest="model_name",
                      help="model name", metavar="MODEL_NAME")
    parser.add_option("-b", "--base", dest="base_model_name",
                      help="base model name", metavar="BASE_MODEL_NAME")
    (options, args) = parser.parse_args()

    #gen_admin( model=options.model_name, base=options.base_model_name, )
    """
    models = ['InfantArvProph',
        'InfantArvProphMod',
        'InfantBirth',
        'InfantBirthData',        
        'InfantBirthExam',
        'InfantBirthArv',
        'InfantBirthFeed',
        'InfantDeath',
        'InfantDeathAssessment',
        'InfantEligibilityFeedingChoice',
        'InfantEligibility',
        'InfantHaart ',
        'InfantHaartMod',
        'InfantNvpAdherence',
        'InfantOffDrug',
        'InfantPrerandoLoss',
        'InfantStudyDrugInit',
        'InfantSurvival',
        'InfantVisit',]
    """
    models = ['MaternalArvPost ',
    'MaternalArvPostMod',
    'MaternalArvPostAdh',
    'MaternalArvPreg ',
    'MaternalArvPregHistory',
    'MaternalConsent',
    'MaternalDeath',
    'MaternalDeathAssessment',
    'MaternalDeath',
    'MaternalEligiblityPost',
    'MaternalEligiblityAnte',
    'MaternalEnroll',
    'MaternalEnrollDem',
    'MaternalEnrollOb',
    'MaternalEnrollMed',
    'MaternalEnrollDx',
    'MaternalEnrollArv',
    'MaternalEnrollClin',
    'MaternalLabDel',
    'MaternalLabDelMed        ',
    'MaternalLabDelDx  ',
    'MaternalLocator',
    'MaternalPostFu',
    'MaternalPostFuDx ',
    'MaternalVisit',]

    print '""" admin """'        
    for m in models:
        gen_admin( model=m, base='MyModelAdmin', )
        
        
    print '""" forms """'        
    for m in models:
        gen_form( model=m, base='forms.ModelForm', )        
