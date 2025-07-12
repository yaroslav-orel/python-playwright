from playwright.sync_api import Page, expect
from testcontainers.core.container import DockerContainer

from pages.BasePage import BasePage


class HeaderSection(BasePage):

    def __init__(self, page: Page, webapp: DockerContainer):
        super().__init__(page, webapp)
        self.header = page.locator("header")
        self.dashboard_button = self.header.get_by_text("Dashboard")
        self.test_cases_button = self.header.get_by_text("Test Cases")
        self.test_runs_button = self.header.get_by_text("Test Runs")
        self.create_new_test_button = self.header.get_by_text("Create new test")
        self.demo_pages_button = self.header.get_by_text("Demo pages")
        self.welcome_text = self.header.locator(".account")
        self.log_out_button = self.header.locator(".logOut")


