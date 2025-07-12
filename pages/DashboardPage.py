from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer

from pages.BasePage import BasePage
from pages.HeaderSection import HeaderSection


class DashboardPage(BasePage):

    def __init__(self, page: Page, webapp: DockerContainer):
        super().__init__(page, webapp)
        self. header = HeaderSection(page, webapp)
