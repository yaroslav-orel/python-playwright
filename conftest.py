import pytest
from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from config import APP_CONTAINER, APP_PORT
from pages.login import LoginPage
from pages.registration import RegisterPage

@pytest.fixture(scope="session", autouse=True)
def container():
    with (DockerContainer(APP_CONTAINER)
          .with_exposed_ports(APP_PORT)
          as webapp):
        wait_for_logs(webapp, "Quit the server with CONTROL-C.")
        yield webapp

@pytest.fixture
def login_page(page: Page, container: DockerContainer):
    yield LoginPage(page, container)

@pytest.fixture
def register_page(page: Page, container: DockerContainer):
    yield RegisterPage(page, container)
