from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.contrib.auth.models import User


class MpepuStatsTest(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        self.browser = webdriver.Firefox()
        self.page = Page(self.browser, self)
        self.page.visit('/admin')

        # log in
        login_form = self.page.form
        login_form.fill('username', by='admin')
        login_form.fill_and_submit('password', by='admin')
        # Page after login
        self.finder = self.page.finder
        self.assertTrue(self.finder.find_link('Statistics'))

    def tearDown(self):
        self.browser.quit()

    def test_clicking_statistics_link_goes_to_statics_home_page(self):
        self.finder.click_link('Statistics')
        self.assertTrue(self.finder.find_link('Infant Deaths'))


class Page(object):
    def __init__(self, webdriver, testcase):
        self.browser = webdriver
        self.testcase = testcase

    def visit(self, url):
        self.browser.get(self.testcase.live_server_url + url)
        self.finder = Finder(self.browser)
        self.form = TestForm(self.browser)


class Finder(object):

    def __init__(self, browser):
        self.page = browser

    def find_link(self, link_text):
        return self.page.find_element_by_link_text(link_text)

    def click_link(self, link_text):
        self.find_link(link_text).click()

    def find_tag(self, tag_name):
        return self.page.find_element_by_tag_name(tag_name)


class TestForm(object):

    def __init__(self, browser):
        self.page = browser

    def fill(self, field_name, by=''):
        input_field = self.page.find_element_by_name(field_name)
        input_field.send_keys(by)
        return input_field

    def fill_and_submit(self, field_name, by=''):
        input_field = self.fill(field_name, by=by)
        input_field.send_keys(Keys.RETURN)

    def submit(self, value):
        button_selector = "input[value='{0}']".format(value)
        submit_button = self.page.find_element_by_css_selector(button_selector)
        submit_button.click()
