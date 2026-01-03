# pytest --headed
# pytest --alluredir=reports/allure-results
# pytest -s -v --html=reports/pytest_report.html
# pytest -s -v --html=reports/pytest_report.html --capture=tee-sys --self-contained-html
# pytest --alluredir=reports/allure-results -v -s --capture=tee-sys


import allure
import pytest
from playwright.sync_api import Page

from pages.locators import PageLogin, PageHome, BASE_URL
from utils.data_for_tests import read_test_data_json

data_language = read_test_data_json("data_tests/data_language.json")

def attach_screenshot(page: Page, name: str = "Скриншот"):
    """Прикрепляет скриншот страницы к Allure-отчету и логирует"""
    screenshot = page.screenshot()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
    print(f"📸 Скриншот сохранён: {name}")

@allure.feature("Локализация")
@allure.story("Выбор языка")
@allure.title("Успешный выбор языка")
@pytest.mark.parametrize("input_value", data_language)
def test_language(page, input_value: str) -> None:
    print("🧪 Начало теста: выбор языка")

    # Зайти на главную страницу
    with allure.step(f"Открыть URL: {BASE_URL}"):
        PageHome(page).navigate()
        print(f"📍 Открыта страница: {BASE_URL}")

    # Выбрать язык
    with allure.step(f"Выбрать язык: {input_value[0]}"):
        PageHome(page).language(input_value)
        print(f"🌐 Выбран язык: {input_value[0]}")

    with allure.step("Нажать кнопку подтверждения языка"):
        PageHome(page).language_button.click()
        print("🔘 Кнопка языка нажата")

    with allure.step("Проверить URL после смены языка"):
        expected_url = BASE_URL + input_value[0] + "/"
        assert page.url == expected_url, f"Ошибка выбора языка: {input_value[0]}"
        print(f"✅ URL совпадает: {page.url}")

    attach_screenshot(page, "Страница после смены языка")



@pytest.mark.parametrize("input_value", [
    ("aaa3@yandex.ru", "!Qazxsw23ed", "!Qazxsw23edc"),
    ("aaa4@yandex.ru", "!Qazxsw23edc", "!Qazxsw23edc")])
def test_registration(page, input_value: str) -> None:
    # Зайти на главную страницу
    PageHome(page).navigate()
    print(page.url)
    # Открыть страницу регистрации
    PageHome(page).login_link.click()
    # Ввести регистрационные данные
    PageLogin(page).registration(input_value[0], input_value[1],input_value[2])
    # Нажать кнопку "Зарегистрироваться"
    PageLogin(page).registration_button.click()

    # Проверить уникальность email
    error_count = PageLogin(page).registration_error.count()
    print("error_count =",error_count)
    if error_count > 0:
        for i in range(error_count):
            print("--->>> Ошибка --->>>", PageLogin(page).registration_error.nth(i).text_content())
    else:
        print(page.url)

@pytest.mark.parametrize("input_value", [
    ("aaa1@yandex.ru", "!Qazxsw23edc"),
    ("aaa2@yandex.ru", "!Qazxsw23edc")])
def test_login(page, input_value: str) -> None:
    # Зайти на главную страницу
    PageHome(page).navigate()
    # Открыть страницу регистрации
    PageHome(page).login_link.click()
    # Ввести регистрационные данные
    PageLogin(page).login(input_value[0], input_value[1])
    # Нажать кнопку "Зарегистрироваться"
    PageLogin(page).login_button.click()
