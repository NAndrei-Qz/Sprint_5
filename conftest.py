import random
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

@pytest.fixture
def registration_data():
    email = f"{random.randint(100, 999)}@mail.ru"
    password = f"pass{random.randint(100, 999)}"
    return {
        "email": email,
        "password": password
    }

@pytest.fixture
def data_for_create_ad():
    ad_name = f"Велосипед bike{random.randint(100, 999)} Pro MAX"
    ad_description = f"Просмотр по договорённости. Территориально - Уралмаш д{random.randint(1, 200)}"
    ad_price = f"{random.randint(50000, 60000)}"
    return {
        "ad_name": ad_name,
        "ad_description": ad_description,
        "ad_price": ad_price
    }
