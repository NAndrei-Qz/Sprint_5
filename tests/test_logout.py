import pytest

from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import TestData


class TestLogout:
    def test_user_can_logout(self, driver):
        # 1. Ждем появление кнопки вход и регистрация и кликаем на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REG_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_AND_REG_BUTTON).click()

        # 2. Ждем появление окна входа и вводим данные авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_WINDOW))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.REGISTERED_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.REGISTERED_USER_PASSWORD)

        # 3. Отправляем форму
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # 4. Ожидание появления кнопки выйти и нажатие на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGOUT_BUTTON))
        driver.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

        # 5. Ожидание появления кнопки вход и регистрация
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REG_BUTTON))

        # 6. Сбор данных для подтверждения выхода
        login_button = driver.find_element(*MainPageLocators.LOGIN_AND_REG_BUTTON)
        avatar = driver.find_elements(*MainPageLocators.USER_AVATAR_BUTTON)
        name = driver.find_elements(*MainPageLocators.USER_NAME)
        
        # 7. Ожидаемый результат: появилась кнопка войти, пропали аватар и имя пользователя
        assert login_button.is_displayed(), "Кнопка вход и регистрация не появилась на странице"
        assert len(avatar) == 0, "Аватар пользователя присутствует на странице"
        assert len(name) == 0, "Имя пользователя присутствует на странице"
