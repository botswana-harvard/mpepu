from apps.mpepu_maternal.models.maternal_consent import MaternalConsent


class InfantDataDecorator(object):

    def __init__(self, infant_data):
        self.infant = infant_data

    def maternalconsent(self):
        return MaternalConsent.objects.filter(subject_identifier=self.relative_identifier())[0]

    def relative_identifier(self):
        return self.registered_subject().relative_identifier

    def pk(self):
        return self.infant.pk

    def subject_identifier(self):
        return self.registered_subject().subject_identifier

    def registered_subject(self):
        return self.infant.registered_subject

    def infant_birth_id(self):
        return self.registered_subject().infantbirth.pk
