from edc.dashboard.section.classes import BaseSectionForDashboardView, site_sections

from .search import InfantSearchByWord


class SectionInfantView(BaseSectionForDashboardView):
    section_name = 'infant'
    section_display_name = 'Infants'
    section_display_index = 30
    section_template = 'section_infant.html'
    dashboard_url_name = 'subject_dashboard_url'
    search = [InfantSearchByWord]
site_sections.register(SectionInfantView)
