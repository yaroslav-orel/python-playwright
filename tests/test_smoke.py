import re
from time import sleep

from playwright.sync_api import Page, expect

import pytest
from testcontainers.core.container import DockerContainer

from conftest import login_page
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage


def test_login_error(login_page: LoginPage):
    error_text = "Your username and password didn't match. Please try again."

    login_page.navigate()
    login_page.login("admin", "password")

    expect(login_page.login_error).to_have_text(error_text)


def test_registration_success(register_page: RegisterPage):
    username = "testuser"
    email = "test@mail.com"
    password = "s1roNgPa77"

    register_page.navigate()
    register_page.register(username, email, password, password)
    dashboard_page = DashboardPage(register_page.page, register_page.webapp)

    expect(dashboard_page.header.welcome_text).to_have_text(f"Hello, {username}")
