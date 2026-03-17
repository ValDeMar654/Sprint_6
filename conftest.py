import pytest
from selenium import webdriver
from urls import scooter_main_page


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(scooter_main_page)
    yield driver
    driver.quit()
