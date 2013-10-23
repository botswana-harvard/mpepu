from edc.dashboard.section.classes import BaseSectionForDashboardView, site_sections
from .search import MaternalSearchByWord


class SectionMaternalView(BaseSectionForDashboardView):
    section_name = 'maternal'
    section_display_name = 'Maternal'
    section_display_index = 20
    section_template = 'section_maternal.html'
    dashboard_url_name = 'subject_dashboard_url'
    search = [MaternalSearchByWord]
site_sections.register(SectionMaternalView)
