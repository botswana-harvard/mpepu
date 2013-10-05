from edc.subject.consent.classes import ConsentHelper


class MaternalEligibilityConsentHelper(ConsentHelper):

    def clean_versioned_field(self, field_value, field, start_datetime, consent_version):
        """Runs checks on a versioned field.

            Version 2
                * If mother wishes to BF and has a CD4 < 250, she must be willing to initiate HAART.
                  Otherwise, feeding_choice, is_cd4_low, maternal_haart fields are not required.
        """
        if getattr(self.get_subject_instance(), 'feeding_choice') == 'Yes':
            if field.name == 'maternal_haart' and getattr(self.get_subject_instance(), 'is_cd4_low'):
                if  field_value == 'No' and getattr(self.get_subject_instance(), 'is_cd4_low') < 250:  # BF and CD4 < 250 so maternal_haart required
                    raise self.get_exception_cls()('Mother must be willing to initiate HAART if feeding choice is BF and '
                                                   'CD4 < 250 for data captured during or after version {2}. [{3}]'.format(field.name, start_datetime, consent_version, field.verbose_name[0:50]))
