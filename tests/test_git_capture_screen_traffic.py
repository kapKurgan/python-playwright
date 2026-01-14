import pytest

from utils.data_for_tests import read_test_data_json

GITHUB_BASE = "https://github.com"
OWNER_PATH = "kapKurgan"
TRAFFIC_PATH = "graphs/traffic"

data_password = read_test_data_json("passwords/password_github.json")
print(data_password)
my_login, my_password = data_password


@pytest.mark.parametrize("input_value", [
    ("testing-using-selenium-and-python"),
    ("Python_API"),
    ("performance-tests"),
    ("testing-user-management-api"),
    ("effective-mobile"),
    ("python-playwright")])
def test_git_capture_screen_traffic(page, input_value: str) -> None:
    page.goto(GITHUB_BASE)

    sign_in_link = page.locator('a.HeaderMenu-link--sign-in[href="/login"]')
    sign_in_link.click()

    input_login = page.locator('#login_field')
    input_login.fill(my_login)

    input_password = page.locator('#password')
    input_password.fill(my_password)

    button_sign_in = page.locator('input[type="submit"][value="Sign in"].btn-primary')
    button_sign_in.click()

