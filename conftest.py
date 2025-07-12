import pytest
from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from config import APP_CONTAINER, APP_PORT
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage

@pytest.fixture(scope="session", autouse=True)
def webapp():
    with (DockerContainer(APP_CONTAINER)
          .with_exposed_ports(APP_PORT)
          as container):
        wait_for_logs(container, "Quit the server with CONTROL-C.")
        yield container

@pytest.fixture
def login_page(page: Page, webapp: DockerContainer):
    yield LoginPage(page, webapp)

@pytest.fixture
def register_page(page: Page, webapp: DockerContainer):
    yield RegisterPage(page, webapp)

