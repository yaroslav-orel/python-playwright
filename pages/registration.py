from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer

from pages.base_page import BasePage

PATH_TO_REGISTER_PAGE = "/register"


class RegisterPage(BasePage):
    def __init__(self, page: Page, webapp: DockerContainer):
        super().__init__(page, webapp)

        self.username_input = self.page.locator("#id_username")
        self.email_input = self.page.locator("#id_email")
        self.password_input = self.page.locator("#id_password1")
        self.password_confirm_input = self.page.locator("#id_password2")
        self.register_input = page.locator("input[value='Register']")

    def register(self, username: str, email: str, password: str, password_confirm: str):
        self.username_input.fill(username)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.password_confirm_input.fill(password_confirm)
        self.register_input.click()

    def navigate(self):
        self._navigate_to(PATH_TO_REGISTER_PAGE)
