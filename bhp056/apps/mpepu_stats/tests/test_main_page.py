from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MainPageTests(TestCase):

    def test_can_visit_statistics_home_page(self):
        home = self.client.get('/mpepu/statistics/')
        self.assertEquals(home.status_code, 200, "main Statistics page should not redirect.")


class StatisticsAppPageTests(LiveServerTestCase):

    # go to main app home page and click the statistics button
    # In the statistics home page click the 'eligible infants' link
    # It should take you to the eligible infants page
    # clicking on an infant pk link should redirect to infant dashboard page
    # clicking on a relative pk link should redirect to maternal dashboard page
    # for mother

    def test_statistics_button_appears_on_homepage(self):
        self.browser.get(self.live_server_url)
