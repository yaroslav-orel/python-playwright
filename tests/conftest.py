import re
from pathlib import Path
from random import randrange

from allure import attachment_type, attach
import pytest
from playwright.sync_api import Page, Browser
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from config import APP_CONTAINER, APP_PORT
from models.user import User
from pages.login import LoginPage
from pages.registration import RegisterPage
from pages.dashboard import DashboardPage

SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.png$")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    yield
    attach_files(item)


@pytest.fixture(scope="session", autouse=True)
def container():
    with DockerContainer(APP_CONTAINER).with_exposed_ports(APP_PORT) as webapp:
        wait_for_logs(webapp, "Quit the server with CONTROL-C.")
        yield webapp


@pytest.fixture
def login_page(page: Page, container: DockerContainer):
    yield LoginPage(page, container)


@pytest.fixture
def register_page(page: Page, container: DockerContainer):
    yield RegisterPage(page, container)


@pytest.fixture
def dashboard_page(page: Page, container: DockerContainer):
    yield DashboardPage(page, container)


@pytest.fixture(scope="session")
def shared_user():
    return User(
        username=f"shareduser{randrange(1000, 9999)}",
        email=f"shared{randrange(1000, 9999)}@test.com",
        password="s1roNgPa77",
    )


@pytest.fixture(scope="session", autouse=True)
def registered_user(shared_user: User, browser: Browser, container: DockerContainer):
    with browser.new_context() as context:
        with context.new_page() as page:
            register_page = RegisterPage(page, container)
            register_page.navigate()
            register_page.register(
                shared_user.username,
                shared_user.email,
                shared_user.password,
                shared_user.password,
            )
    return shared_user


def create_user_and_login(
    register_page: RegisterPage, login_page: LoginPage, user: User
) -> DashboardPage:
    """Helper function to register a user and login."""
    register_page.navigate()
    register_page.register(user.username, user.email, user.password, user.password)
    dashboard_page = DashboardPage(register_page.page, register_page.webapp)

    # Logout to prepare for login
    dashboard_page.header.log_out_button.click()

    # Login with the user
    login_page.login(user.username, user.password)
    return dashboard_page


def register_user(register_page: RegisterPage, user: User) -> DashboardPage:
    """Helper function to register a user and return dashboard page."""
    register_page.navigate()
    register_page.register(user.username, user.email, user.password, user.password)
    return DashboardPage(register_page.page, register_page.webapp)


def attach_files(item):
    artifacts_dir = item.funcargs.get("output_path")
    if artifacts_dir:
        artifacts_dir_path = Path(artifacts_dir)
        if artifacts_dir_path.is_dir():
            for file in artifacts_dir_path.iterdir():
                if file.is_file() and SCREENSHOT_NAME_PATTERN.match(file.name):
                    attach.file(
                        str(file), name=file.name, attachment_type=attachment_type.PNG
                    )
                elif file.is_file() and file.suffix == ".webm":
                    attach.file(
                        file, name=file.name, attachment_type=attachment_type.WEBM
                    )
