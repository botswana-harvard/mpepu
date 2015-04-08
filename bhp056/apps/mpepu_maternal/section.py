from edc.dashboard.section.classes import BaseSectionView, site_sections
from .search import MaternalSearchByWord
from .models import MaternalConsent


class SectionMaternalView(BaseSectionView):
    section_name = 'maternal'
    section_display_name = 'Maternal'
    section_display_index = 20
    section_template = 'section_maternal.html'
    dashboard_url_name = 'subject_dashboard_url'
    add_model = MaternalConsent
    search = {'word': MaternalSearchByWord}
    show_most_recent = True

site_sections.register(SectionMaternalView)
