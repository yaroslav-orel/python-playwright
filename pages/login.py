from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer

from pages.base_page import BasePage

PATH_TO_LOGIN = "/login/"

class LoginPage(BasePage):
    def __init__(self, page: Page, container: DockerContainer):
        super().__init__(page, container)

        self.username_input = page.locator("#id_username")
        self.password_input = page.locator("#id_password")
        self.register_button = page.get_by_text("Don't have account yet?")
        self.login_button = page.locator("input[value='Login']")
        self.login_error = page.locator(".loginError")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def navigate(self):
        self._navigate_to(PATH_TO_LOGIN)
