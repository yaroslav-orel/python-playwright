from random import randrange

from playwright.sync_api import expect

from models.user import User
from pages.dashboard import DashboardPage
from pages.login import LoginPage, PATH_TO_LOGIN
from pages.registration import RegisterPage
from tests.conftest import create_user_and_login, register_user


def test_login_error(login_page: LoginPage):
    error_text = "Your username and password didn't match. Please try again."

    login_page.navigate()
    login_page.login("admin", "password")

    expect(login_page.login_error).to_have_text(error_text)


def test_registration_success(register_page: RegisterPage):
    user = User(
        username=f"testuser{randrange(1000, 9999)}",
        email=f"test{randrange(1000, 9999)}@mail.com",
        password="s1roNgPa77",
    )

    dashboard_page = register_user(register_page, user)
    expect(dashboard_page.header.welcome_text).to_have_text(f"Hello, {user.username}")


def test_successful_login(register_page: RegisterPage, login_page: LoginPage):
    user = User(
        username=f"loginuser{randrange(1000, 9999)}",
        email=f"login{randrange(1000, 9999)}@test.com",
        password="s1roNgPa77",
    )

    dashboard_page = create_user_and_login(register_page, login_page, user)
    expect(dashboard_page.header.welcome_text).to_have_text(f"Hello, {user.username}")


def test_registration_password_mismatch(register_page: RegisterPage):
    user = User(
        username=f"mismatchuser{randrange(1000, 9999)}",
        email=f"mismatch{randrange(1000, 9999)}@test.com",
        password="s1roNgPa77",
    )
    password_confirm = "differentPassword123"

    register_page.navigate()
    register_page.register(user.username, user.email, user.password, password_confirm)

    expect(register_page.registration_errors.first).to_contain_text(
        "The two password fields didn’t match."
    )


def test_logout_functionality(
    shared_user: User, login_page: LoginPage, dashboard_page: DashboardPage
):
    login_page.navigate()
    login_page.login(shared_user.username, shared_user.password)

    # Logout
    dashboard_page.header.log_out_button.click()

    # Verify redirected to login page
    expect(login_page.page).to_have_url(f"{login_page.base_url}{PATH_TO_LOGIN}")
