from edc.dashboard.subject.classes import RegisteredSubjectDashboard


class DashboardMixin(object):

    @RegisteredSubjectDashboard.locator_model.getter
    def locator_model(self):
        return self.get_locator_model()

    def render_labs(self):
        super(DashboardMixin, self).render_labs()

    def add_to_context(self):
        super(DashboardMixin, self).add_to_context()
        self.context.add(scheduled_lab_bucket=True)
