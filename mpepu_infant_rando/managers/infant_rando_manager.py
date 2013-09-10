#from datetime import datetime
from django.db import models
#from django.db.models import Q
#from mpepu_infant.models import InfantBirth
from mpepu_infant_rando.classes import Randomization


class InfantRandoManager(models.Manager):

    def randomize(self, **kwargs):
        infant_eligibility = kwargs.get('infant_eligibility')
        return Randomization().randomize(infant_eligibility)

#        """Selects the next available record from the infant_rando model that matches the given criteria.
#
#        Criteria are site and stratum (based on feeding choice and HAART status)
#        """
#        infant_eligibility = kwargs.get('infant_eligibility')
#        if infant_eligibility:
#            maternal_feeding_choice = infant_eligibility.maternal_feeding_choice
#            maternal_art_status = infant_eligibility.maternal_art_status
#            site = infant_eligibility.randomization_site
#            registered_subject = infant_eligibility.registered_subject
#        user = ""
#        infant_initials = registered_subject.initials
#        if super(InfantRandoManager, self).filter(subject_identifier=registered_subject.subject_identifier):
#            # you should have caught this in the ModelForm !!
#            raise TypeError('Subject already randomized. Got %s' % (registered_subject))
#        if maternal_feeding_choice == 'FF':
#            stratum = 'FF'
#        elif maternal_feeding_choice == 'BF' and maternal_art_status == 'ON':
#            stratum = 'BF,HAART'
#        elif maternal_feeding_choice == 'BF' and maternal_art_status == 'OFF':
#            stratum = 'BF,notHAART'
#        else:
#            raise TypeError('Cannot determine stratum. Got %s and %s' % (maternal_feeding_choice, maternal_art_status))
#        infant_rando = super(InfantRandoManager, self).filter(
#                                            Q(site__exact=site),
#                                            Q(stratum__exact=stratum),
#                                            (Q(subject_identifier__isnull=True) |
#                                            Q(subject_identifier=''))
#                                            ).order_by('sid')
#        if infant_rando:
#            # TODO: handle twins + so they all have same assignment
#            #if registered_subject.subject_identifier[0:-2]+'-25'
#            #get sid for first twin, triplet
#            #modify this sid so that feeding and rx are the same as first
#            dte = datetime.today()
#            infant_rando[0].subject_identifier = registered_subject.subject_identifier
#            infant_rando[0].haart_status = maternal_art_status
#            infant_rando[0].feeding_choice = maternal_feeding_choice
#            infant_rando[0].randomization_datetime = dte
#            infant_rando[0].infant_initials = infant_initials
#            infant_rando[0].dispensed = 'NO'
#            infant_rando[0].user_modified = user
#            infant_rando[0].modified = dte
#            infant_rando[0].save()
#            registered_subject.sid = infant_rando[0].sid
#            registered_subject.user_modified = user
#            registered_subject.first_name = InfantBirth.objects.get(registered_subject=registered_subject).first_name
#            registered_subject.initials = infant_initials
#            registered_subject.randomization_datetime = infant_rando[0].randomization_datetime
#            registered_subject.modified = dte
#            registered_subject.registration_status = 'RANDOMIZED'
#            registered_subject.save()
#            return infant_rando
#        else:
#            return False
