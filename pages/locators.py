from playwright.sync_api import Page

BASE_URL = "http://selenium1py.pythonanywhere.com/"

class PageHome:
    def __init__(self, page: Page):
        self.page = page
        self.login_link = page.locator("#login_link")
        self.language_selector = page.locator("#language_selector > div > select")
        self.language_button = page.locator("#language_selector > button")

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto(BASE_URL)

    def language(self, language: str):
        self.language_selector.select_option(language)


class PageLogin:
    def __init__(self, page: Page):
        self.page = page
        self.registration_email = page.locator('#id_registration-email')
        self.registration_password_1 = page.locator('#id_registration-password1')
        self.registration_password_2 = page.locator('#id_registration-password2')
        self.registration_button = page.locator('#register_form > button')
        self.registration_error = page.locator('#register_form > div.form-group.has-error > div > span')
        self.registration_error_alert = page.locator('#register_form > div.alert.alert-danger')


        self.login_email = page.locator("#id_login-username")
        self.login_password = page.locator('#id_login-password')
        self.login_button = page.locator('#login_form > button')

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto(BASE_URL)

    def registration(self, email: str, password_1: str, password_2: str):
        self.registration_email.fill(email)
        self.registration_password_1.fill(password_1)
        self.registration_password_2.fill(password_2)

    def login(self, email: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.login_email.fill(email)
        self.login_password.fill(password)
