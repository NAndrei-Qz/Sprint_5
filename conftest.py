import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.DESK_URL)
    yield driver
    driver.quit()


