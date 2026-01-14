# pytest -m include_slow


import allure
import pytest
from datetime import datetime
from utils.data_for_tests import read_test_data_json

GITHUB_BASE = "https://github.com"
OWNER_PATH = "kapKurgan"
TRAFFIC_PATH = "graphs/traffic"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
data_password = read_test_data_json("passwords/password_github.json")
my_login, my_password = data_password

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        "viewport": {
            "width": 1600,
            "height": 800,
        }
    }

@allure.feature("GitHub")
@allure.story("Уникальные пользователи")
@pytest.mark.skipif("'include_slow' not in config.option.markexpr",
    reason="пропущено по умолчанию, запускается с -m include_slow"
)
@pytest.mark.include_slow
@pytest.mark.parametrize("input_value", [
    ("testing-using-selenium-and-python"),
    ("Python_API"),
    ("performance-tests"),
    ("testing-user-management-api"),
    ("effective-mobile"),
    ("python-playwright")])
def test_git_capture_screen_traffic(page, input_value: str) -> None:
    allure.dynamic.title(input_value)

    page.goto(GITHUB_BASE)

    sign_in_link = page.locator('a.HeaderMenu-link--sign-in[href="/login"]')
    sign_in_link.click()

    input_login = page.locator('#login_field')
    input_login.fill(my_login)

    input_password = page.locator('#password')
    input_password.fill(my_password)

    button_sign_in = page.locator('input[type="submit"][value="Sign in"].btn-primary')
    button_sign_in.click()

    page.goto(f'{GITHUB_BASE}/{OWNER_PATH}/{input_value}/{TRAFFIC_PATH}')

    setup_graphs = page.locator('#repo-content-pjax-container > div > div > div.Layout-main > react-app > div > div > div:nth-child(4) > div:nth-child(2) > div > div.Box-sc-62in7e-0.fsypPW.ChartCard-module__ChartCardHeaderContainer--FAjoQ > div.ChartCard-module__ChartCardActionsContainer--s_1yW > button:nth-child(4)')
    setup_graphs.click()

    setup_graphs_swith = page.locator('#__primerPortalRoot__ > div > div > div > div.prc-ScrollableRegion-ScrollableRegion--xtjK.prc-Dialog-DialogOverflowWrapper-JvHzz > div > div:nth-child(2) > div.prc-ToggleSwitch-ToggleSwitch-rQz-0 > button')
    setup_graphs_swith.click()

    setup_graphs_exit = page.locator('#__primerPortalRoot__ > div > div > div > div.prc-Dialog-Header-f7Me- > div > button')
    setup_graphs_exit.click()

    element = page.locator('#repo-content-pjax-container > div > div > div.Layout-main > react-app > div > div > div:nth-child(4) > div:nth-child(2) > div')
    # element.screenshot(path=f"screenshot/{input_value}_{timestamp}.png")

    screenshot = element.screenshot(path=f"screenshot/{input_value}_{timestamp}.png")
    allure.attach(screenshot, name=f"{input_value}_{timestamp}", attachment_type=allure.attachment_type.PNG)
