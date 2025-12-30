# pytest --headed
import pytest
from pages.locators import PageLogin, PageHome, BASE_URL
from utils.data_for_tests import read_test_data_json

data_language = read_test_data_json("data_tests/data_language.json")

@pytest.mark.parametrize("input_value", data_language)
def test_language(page, input_value: str) -> None:
    # Зайти на главную страницу
    PageHome(page).navigate()
    print(BASE_URL+input_value[0]+"/")
    # Выбрать язык
    PageHome(page).language(input_value)
    PageHome(page).language_button.click()
    # assert page.url == BASE_URL+input_value[0]+"/" f"Ошибка выбора языка {input_value[0]}"
    assert page.url == BASE_URL+input_value[0]+"/", f"Ошибка выбора языка: {input_value[0]}"
    print(page.url)



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
            print("--->>> Ошибка --->>>", PageLogin(page).registration_email_error.nth(i).text_content())
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
