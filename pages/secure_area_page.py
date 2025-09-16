# pages/secure_area_page.py
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class SecureAreaPage:
    LOGOUT_BUTTON = (By.XPATH,"//a[text()='Log out']")
    success_message = (By.XPATH,"//h1[text()='Logged In Successfully']")
    try:
        def __init__(self, driver):
            self.driver = driver

        def is_logout_button_displayed(self):
            result = self.driver.find_element(*self.LOGOUT_BUTTON).is_displayed()
            print("displayed")
            return result

        def is_success_message_displayed(self):
            res = self.driver.find_element(*self.success_message).is_displayed()
            print("success message")
            return res

        def click_logout_button(self):
            self.driver.find_element(*self.LOGOUT_BUTTON).click()

    except NoSuchElementException as e:
        print("An error occurred",e)