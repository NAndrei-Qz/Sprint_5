from selenium.webdriver.common.by import By

# --- ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ РЕГИСТРАЦИИ ---
class RegistrationPageLocators:
    REG_EMAIL_INPUT = (By.NAME, "email")
    REG_PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_REG_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    EMAIL_ERROR = (By.XPATH, ".//form/div/div/span[text()='Ошибка']")
    EMAIL_INPUT_REDLINE = (By.XPATH, ".//input[@name='email']/parent::div")
    PASSWORD_INPUT_REDLINE = (By.XPATH, ".//input[@name='password']/parent::div")
    SUBMIT_PASSWORD_INPUT_REDLINE = (By.XPATH, ".//input[@name='submitPassword']/parent::div")
    REGISTRATION_WINDOW = (By.CLASS_NAME, "h1")

# --- ЛОКАТОРЫ ДЛЯ ГЛАВНОЙ СТРАНИЦЫ ---
class MainPageLocators:
    LOGIN_AND_REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    USER_AVATAR_BUTTON = (By.CLASS_NAME, "circleSmall")
    USER_NAME = (By.CSS_SELECTOR, ".profileText.name")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    CREATE_AD_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    SEARCH_INPUT = (By.CLASS_NAME, "input_inputDefaultSearch__EKhe3")

# --- ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ ВХОДА---
class LoginPageLocators:
    LOGIN_WINDOW = (By.CLASS_NAME, "h1")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    NEW_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

# --- ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ СОЗДАНИЯ ОБЪЯВЛЕНИЯ---
class CreateAdPageLocators:
    SIGNIN_FOR_CREATE_AD = (By.CLASS_NAME, "h1")
    AD_NAME_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']") 
    DROP_DOWN_MENU_CATEGORY = (By.XPATH, ".//div[@class='createListing_inputRow__fmwXw']/div/div/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    DROP_DOWN_MENU_CITY = (By.XPATH, ".//form/div[@class='dropDownMenu_dropMenu__sBxhz']/div/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    DROP_DOWN_MENU_EKB = (By.XPATH, ".//span[text()='Екатеринбург']")
    DROP_DOWN_MENU_HOBBI = (By.XPATH, ".//span[text()='Хобби']")
    RADIO_BUTTON_NEW = (By.XPATH, ".//div[@class='radioUnput_inputActive__eC-HY']")
    PRICE_INPUT = (By.NAME, "price")
    AD_POST_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")

# --- ЛОКАТОРЫ ДЛЯ СТРАНИЦЫ ПРОФИЛЯ---
class ProfilePageLocators:
    MY_ADDED_CARDS = (By.XPATH, ".//div[@class='about']/h2")
    MY_PROFILE = (By.XPATH, ".//h1[text()='Мой профиль']")
    MY_CARDS_NEXT_PAGE = (By.XPATH, ".//button[@class='arrowButton arrowButton--right undefined']")

        