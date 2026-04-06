import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/FileDownload.html")

    yield driver
    driver.quit()


def test_demo(driver):
    driver.find_element(By.XPATH,"//a[@type='button']").click()