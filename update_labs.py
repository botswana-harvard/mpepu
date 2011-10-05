#!/usr/bin/env python
def main():
    registered_subjects = RegisteredSubject.objects.all()
    for registered_subject in registered_subjects:
        subject_identifier = registered_subject.subject_identifier
        labs = Lab.objects.fetch(subject_identifier=subject_identifier)
        if labs:
            results = Result.objects.fetch(subject_identifier=subject_identifier, labs=labs)
            if results:
                x= ResultItem.objects.fetch(subject_identifier=subject_identifier, results=results)
        print subject_identifier     

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

    main()
