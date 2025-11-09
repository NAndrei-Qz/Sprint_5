import pytest

from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import TestData


class TestLogin:
    def test_user_can_login(self, driver):
        # 1. Ждем появление кнопки вход и регистрация и кликаем на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REG_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_AND_REG_BUTTON).click()

        # 2. Ждем появление окна входа и вводим данные авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_WINDOW))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.REGISTERED_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.REGISTERED_USER_PASSWORD)

        # 3. Отправляем форму
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # 4. Ожидание появления элементов профиля
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.USER_AVATAR_BUTTON))

        # 5. Сбор данных для подтверждения регистрации
        avatar_class = driver.find_element(*MainPageLocators.USER_AVATAR_BUTTON).get_attribute("class")
        user_name = driver.find_element(*MainPageLocators.USER_NAME).text
        search_string = driver.find_element(*MainPageLocators.SEARCH_INPUT)

        # 6. Ожидаемый результат: на главной странице, у клавиши "Разместить объявление" отображается аватар пользователя и имя "User."
        assert search_string.is_displayed(), "Не найдена строка поиска, возможно не произошел переход на главную страницу"
        assert avatar_class == "circleSmall", "На странице отсутствует Аватар пользователя"
        assert user_name == "User.", "На странице отсутствует имя пользователя"
