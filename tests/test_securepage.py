from pages.secure_area_page import SecureAreaPage


def test_sp(driver):
    driver.get("https://practicetestautomation.com/logged-in-successfully/")

    secure_page = SecureAreaPage(driver)

    secure_page.is_logout_button_displayed()
    secure_page.click_logout_button()