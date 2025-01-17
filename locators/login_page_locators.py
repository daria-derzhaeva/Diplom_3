from selenium.webdriver.common.by import By

class LoginPageLocators:

    INPUT_NAME = By.XPATH, "//input[@name='name']"
    INPUT_PASSWORD = By.XPATH, "//input[@name='Пароль']"
    LOGIN_BUTTON = By.XPATH, "//Button[text()='Войти']"
    PASSWORD_RECOVERY = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"