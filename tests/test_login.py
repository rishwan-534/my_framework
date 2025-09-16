# tests/test_login.py

from pages.login_page import LoginPage


def test_successful_login(driver,base_url):
    login_page = LoginPage(driver)
    login_page.open(base_url)
    secure_area_page = login_page.login("student", "Password123")
    print(secure_area_page)
    assert secure_area_page.is_logout_button_displayed()
    print("Assertion Passed")


