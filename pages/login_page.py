from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.secure_area_page import SecureAreaPage


class LoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    try:

        def __init__(self, driver):
            self.driver = driver

        def open(self, base_url):
            self.driver.get(base_url)

        def set_username(self, username):
            self.driver.find_element(*self.USERNAME_INPUT).clear()
            self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

        def set_password(self, password):
            self.driver.find_element(*self.PASSWORD_INPUT).clear()
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        def click_login(self):
            self.driver.find_element(*self.SUBMIT_BUTTON).click()
            # return SecureAreaPage(self.driver)

        def login(self, username, password):
            self.set_username(username)
            self.set_password(password)
            self.click_login()
            return SecureAreaPage(self.driver)

    except NoSuchElementException as e:
        print("An error occurred",e)
