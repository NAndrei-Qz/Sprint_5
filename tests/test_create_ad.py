import pytest

from locators import MainPageLocators, LoginPageLocators, CreateAdPageLocators, ProfilePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from data import TestData
from helpers import GenerationData


class TestCreateAd:
    def test_create_ad_without_auth(self, driver):
        # 1. Ждем появление кнопки разместить объявление и кликаем на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.CREATE_AD_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        # 2. Ждем появление окна, в котором требуется войти или зарегистрироваться
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(CreateAdPageLocators.SIGNIN_FOR_CREATE_AD))
        # 3. Сбор данных
        auth_window = driver.find_element(*CreateAdPageLocators.SIGNIN_FOR_CREATE_AD)
        text_in_window = driver.find_element(*CreateAdPageLocators.SIGNIN_FOR_CREATE_AD).text

        #4 . Ожидаемый результат: Появилось окно с просьбой авторизоваться"
        assert auth_window.is_displayed(), "Окно с просьбой авторизоваться не появилось"
        assert text_in_window == "Чтобы разместить объявление, авторизуйтесь", "Сообщение с просьбой авторизоваться не совпадает с ожидаемым результатом"

    def test_create_ad_after_auth(self, driver):
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

        # 5. Ищем кнопку создания объявления и кликаем
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        # 6. Ждем появление элементов на странице создания объявления и заполняем
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(CreateAdPageLocators.AD_NAME_INPUT))
        driver.find_element(*CreateAdPageLocators.AD_NAME_INPUT).send_keys(GenerationData.AD_NAME)
        driver.find_element(*CreateAdPageLocators.DROP_DOWN_MENU_CATEGORY).click()
        driver.find_element(*CreateAdPageLocators.DROP_DOWN_MENU_HOBBI).click()
        driver.find_element(*CreateAdPageLocators.RADIO_BUTTON_NEW).click()
        driver.find_element(*CreateAdPageLocators.DROP_DOWN_MENU_CITY).click()
        driver.find_element(*CreateAdPageLocators.DROP_DOWN_MENU_EKB).click()
        driver.find_element(*CreateAdPageLocators.DESCRIPTION_INPUT).send_keys(GenerationData.AD_DESCRIPTION)
        driver.find_element(*CreateAdPageLocators.PRICE_INPUT).send_keys(GenerationData.AD_PRICE)

        # 7. Отправляем форму и ждём перехода на главную страницу (ждем появление строки поиска)
        driver.find_element(*CreateAdPageLocators.AD_POST_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.SEARCH_INPUT))

        # 8. Переходим в мой профиль, дождиаемся появления заголовка
        driver.find_element(*MainPageLocators.USER_AVATAR_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.MY_PROFILE))

        # 9. Листаем до последней страницы, так как новое объявление появляется там
        while True:
            try:
                #Если кнопка следующей страницы кликабельна, значит мы еще не на последней странице, следоавтально кликаем на нее и ждем появления карточек
                next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ProfilePageLocators.MY_CARDS_NEXT_PAGE))
                next_button.click()
                WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.MY_ADDED_CARDS))
            except TimeoutException:
                #Когда кнопка не стала кликабельной в течение ожидания 5с (значит мы на последней странице), ловим исключение и выходим из цикла
                break

        # 10. #Получаем список элементов с названиями карточек на странице
        # Затем для каждого элемента получаем текст названия с помощью метода text и записываем в список
        # ищем среди всех названий карточек на странице именно то название объявления, которое добавили в рамках теста
        elements_list = driver.find_elements(*ProfilePageLocators.MY_ADDED_CARDS)
        cards_name_list = [element.text for element in elements_list]

        assert GenerationData.AD_NAME in cards_name_list, "В разделе Мои объявления отсутствует созданное объявление"
