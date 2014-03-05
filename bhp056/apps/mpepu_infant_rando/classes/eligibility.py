from datetime import date
from django import forms


class Eligibility(object):

    def check(self, current_consent_version, dob, ga=None, weight=None, clinical_jaundice=None, anemia_neutropenia=None, today=None, exception_cls=None, suppress_exception=False):
        if not exception_cls:
            exception_cls = forms.ValidationError
        if not isinstance(dob, date):
            raise TypeError('DoB must be an instance of datetime.date')
        allow_rando = False
        msg = []
        if not today:
            today = date.today()
        # IMPORTANT: days of life are 1-base index not 0-base so >=28 <=34 becomes >=27 <=33
        td = today - dob
        if current_consent_version == 1:
            if td.days < 27 or td.days > 33:
                if not suppress_exception:
                    raise exception_cls('Randomization failed for version 1. Infant must be aged between 28 and 34 days inclusive. Got %s days.' % td.days)
            else:
                allow_rando = True
        elif current_consent_version >= 2:
            if (date.today() - dob).days < 0:
                if not suppress_exception:
                    raise exception_cls('Randomization failed. dob is in the future or system time is wrong!. Got {0}'.format(date.today() - dob).days)
            elif abs((date.today() - dob).days) < 13:
                # no matter what, infant must be 13 days or more old
                if not suppress_exception:
                    raise exception_cls('Randomization failed. Infant must be 14 days of life or older to verify eligibility. Got {0}'.format(abs((date.today() - dob).days)))
            elif abs((date.today() - dob).days) > 33:
                # no matter what, infant must be less than 33 days old
                if not suppress_exception:
                    raise exception_cls('Randomization failed. Infant must be 34 days of life or younger to verify eligibility. Got {0}'.format(abs((date.today() - dob).days)))
            else:
                if ga >= 36:
                    msg.append('maternal GA must be >= 36 weeks')
                    if td.days >= 13 and td.days < 27:
                        msg.append('infant aged between 14 and 28 days')
                        if weight >= 2.5 and clinical_jaundice == 'No' and anemia_neutropenia == 'No':
                            allow_rando = True
                        else:
                            msg.append('infant weight must be >= 2.5kg and/or infant may not have any of jaundice/anemia/neutropenia')
                    elif td.days >= 27 and td.days <= 33 and clinical_jaundice == 'No' and anemia_neutropenia == 'No':
                        msg.append('infant aged between 28 and 34 days')
                        allow_rando = True
                    else:
                        if not suppress_exception:
                            raise exception_cls('Randomization failed. Infant must be aged between 28 and 34 days. Got {0} days. Correct or complete Pre-eligibility form.'.format(td.days))
                elif ga < 36:
                    msg.append('maternal GA must be < 36 weeks')
                    if td.days >= 27 and td.days <= 33 and clinical_jaundice == 'No' and anemia_neutropenia == 'No':
                        allow_rando = True
                    else:
                        msg.append('infant must be aged between 28 and 34 days and/or infant may not have any of jaundice/anemia/neutropenia')
        else:
            if not suppress_exception:
                raise exception_cls('Randomization failed. Version of the maternal consent is invalid. Contact the Data Manager.')
        if not allow_rando:
            if not suppress_exception:
                raise exception_cls('Randomization failed. {0}. Correct or complete Pre-eligibility form.'.format(' and '.join(msg)))
        return allow_rando
