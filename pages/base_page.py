from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer

from config import APP_PORT


class BasePage:

    def __init__(self, page: Page, webapp: DockerContainer):
        self.page = page
        self.webapp = webapp
        self.base_url = f"http://{webapp.get_container_host_ip()}:{webapp.get_exposed_port(APP_PORT)}"

    def open_app(self):
        self.page.goto(self.base_url)

    def _navigate_to(self, path: str):
        self.page.goto(self.base_url + path)
