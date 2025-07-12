from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer

from pages.base_page import BasePage
from pages.header import HeaderSection


class DashboardPage(BasePage):

    def __init__(self, page: Page, webapp: DockerContainer):
        super().__init__(page, webapp)
        self. header = HeaderSection(page, webapp)
