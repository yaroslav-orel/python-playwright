import re
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from config import APP_CONTAINER, APP_PORT
from pages.login import LoginPage
from pages.registration import RegisterPage

SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.png$")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    yield

    artifacts_dir = item.funcargs.get("output_path")
    if artifacts_dir:
        artifacts_dir_path = Path(artifacts_dir)
        if artifacts_dir_path.is_dir():
            for file in artifacts_dir_path.iterdir():
                if file.is_file() and SCREENSHOT_NAME_PATTERN.match(file.name):
                    allure.attach.file(str(file), name=file.name, attachment_type=allure.attachment_type.PNG)
                elif file.is_file() and file.suffix == ".webm":
                    allure.attach.file(file, name=file.name, attachment_type=allure.attachment_type.WEBM)


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
