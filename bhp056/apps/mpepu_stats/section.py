from edc.dashboard.section.classes import BaseSectionView, site_sections


class SectionStatisticsView(BaseSectionView):
    section_name = 'statistics'
    section_display_name = 'Statistics'
    section_display_index = 40
    section_template = 'section_statistics.html'
    dashboard_url_name = 'subject_dashboard_url'

site_sections.register(SectionStatisticsView)
