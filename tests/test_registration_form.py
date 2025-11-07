import pytest

from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import TestData


class TestRegistrationNewUser:
    def test_user_can_register(self, driver, registration_data):
        # 1. Ждем появление кнопки вход и регистрация и кликаем на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REG_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_AND_REG_BUTTON).click()

        # 2. Ожидание окна входа и переход к регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_WINDOW))
        driver.find_element(*LoginPageLocators.NEW_ACCOUNT_BUTTON).click()

        # 3. Ожидание окна регистрации и ввод данных регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(registration_data["email"])
        driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(registration_data["password"])
        driver.find_element(*RegistrationPageLocators.SUBMIT_REG_PASSWORD_INPUT).send_keys(registration_data["password"])

        # 4. Отправка формы
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        # 5. Ожидание появления элементов профиля
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.USER_AVATAR_BUTTON))

        # 6. Сбор данных для подтверждения регистрации
        avatar_class = driver.find_element(*MainPageLocators.USER_AVATAR_BUTTON).get_attribute("class")
        user_name = driver.find_element(*MainPageLocators.USER_NAME).text
        search_string = driver.find_element(*MainPageLocators.SEARCH_INPUT)

        # 7. Ожидаемый результат: на главной странице, у клавиши "Разместить объявление" отображается аватар пользователя и имя "User."
        assert search_string.is_displayed(), "Не найдена строка поиска, возможно не произошел переход на главную страницу"
        assert avatar_class == "circleSmall", "На странице отсутствует Аватар пользователя"
        assert user_name == "User.", "На странице отсутствует имя пользователя"

    def test_registration_with_email_error(self, driver):
        # 1. Ждем появление кнопки вход и регистрация и кликаем на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REG_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_AND_REG_BUTTON).click()

        # 2. Ожидание окна входа и переход к регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_WINDOW))
        driver.find_element(*LoginPageLocators.NEW_ACCOUNT_BUTTON).click()

        # 3. Ожидание окна регистрации и ввод данных с некорректной формой почты
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(TestData.USER_EMAIL_NEGATIVE)
        driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD_NEGATIVE)
        driver.find_element(*RegistrationPageLocators.SUBMIT_REG_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD_NEGATIVE)

        # 4. Отправка формы
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        
        # 5. Ожидание появления ошибки и сбор данных        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR))
        email_redline = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT_REDLINE)
        password_redline = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT_REDLINE)
        submit_password_redline = driver.find_element(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT_REDLINE)
        email_error = driver.find_element(*RegistrationPageLocators.EMAIL_ERROR)

        # 6. Ожидаемый результат: поля регистрации обведены красной линией, под полем "Email" - "Ошибка"
        assert email_redline.is_displayed(), "Красная рамка у поля email не отображается"
        assert password_redline.is_displayed(), "Красная рамка у поля password не отображается"
        assert submit_password_redline.is_displayed(), "Красная рамка у поля submit_password не отображается"
        assert email_error.is_displayed(), "Сообщение об ошибке email не отображается"

    def test_email_duplication(self, driver):
        # 1. Ждем появление кнопки вход и регистрация и кликаем на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REG_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_AND_REG_BUTTON).click()

        # 2. Ждем появление окна входа и переходим к регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_WINDOW))
        driver.find_element(*LoginPageLocators.NEW_ACCOUNT_BUTTON).click()

        # 3. Ждем появление окна регистрации и вводим данные существующего пользователя, полученные из фикстуры
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(TestData.REGISTERED_USER_EMAIL)
        driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(TestData.REGISTERED_USER_PASSWORD)
        driver.find_element(*RegistrationPageLocators.SUBMIT_REG_PASSWORD_INPUT).send_keys(TestData.REGISTERED_USER_PASSWORD)

        # 4. Отправка формы
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        # 5. Ожидание появления ошибки и сбор данных
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR))
        email_redline = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT_REDLINE)
        password_redline = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT_REDLINE)
        submit_password_redline = driver.find_element(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT_REDLINE)
        email_error = driver.find_element(*RegistrationPageLocators.EMAIL_ERROR)

        # 6. Ожидаемый результат: поля регистрации обведены красной линией, под полем "Email" - "Ошибка"
        assert email_redline.is_displayed(), "Красная рамка у поля email не отображается"
        assert password_redline.is_displayed(), "Красная рамка у поля password не отображается"
        assert submit_password_redline.is_displayed(), "Красная рамка у поля submit_password не отображается"
        assert email_error.is_displayed(), "Сообщение об ошибке email не отображается"
