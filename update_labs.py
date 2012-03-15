#!/usr/bin/env python
def main():
    registered_subjects = RegisteredSubject.objects.all()
    total = registered_subjects.count()
    cnt = 0
    for registered_subject in registered_subjects:
        
        subject_identifier = registered_subject.subject_identifier

        dmis = Dmis()
        dmis.fetch(subject_identifier=subject_identifier, lab_db='lab_api')

        dmis = DmisReceive()
        dmis.fetch(subject_identifier=subject_identifier, lab_db='lab_api')
        dmis = DmisOrder()
        dmis.fetch(subject_identifier=subject_identifier, lab_db='lab_api')
        
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

    import sys, os
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


    main()
