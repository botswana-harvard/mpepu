from collections import namedtuple

from edc.dashboard.section.classes import BaseSectionView, site_sections


ModelMeta = namedtuple('ModelMeta', 'app_label model_name')


class SectionAdministrationView(BaseSectionView):
    section_name = 'administration'
    section_display_name = 'Administration'
    section_display_index = 140
    section_template = 'mpepu_section_administration.html'

site_sections.register(SectionAdministrationView, replaces='administration')


class SectionAppointmentView(BaseSectionView):
    section_name = 'appointments'
    section_display_name = 'Appointments'
    section_display_index = 110
    section_template = 'mpepu_section_appointment.html'

site_sections.register(SectionAppointmentView, replaces='appointments')