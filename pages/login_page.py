import allure
from selenium.webdriver.common.by import By

from pages.top_bars.top_menu_bar import TopMenuBar


class LoginPage(TopMenuBar):
    """ Login Page """
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[type=email]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type=password]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//div[@class='absolute ml-0 mt-0.5 text-red-500 text-sm truncate inset-x-0']")
   # PAGE_TITLE = (By.CSS_SELECTOR, ".e-form-heading")
    PAGE_TITLE = (By.XPATH, "//head")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[href='https://app.involve.me/password/reset']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Log in with username: {username} and password: {password}")
    def login(self, username: str, password: str):
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Get error message")
    def get_error_message(self) -> str:
        print("dhshdhs",self.LOGIN_ERROR_MESSAGE)
        return self.get_text(self.LOGIN_ERROR_MESSAGE)


    @allure.step("Get page title")
    def get_page_title(self) -> str:
        return self._driver.title

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self) -> None:
        self.click(self.FORGOT_PASSWORD_LINK)
