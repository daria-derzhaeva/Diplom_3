from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:

    ORDER_HISTORY = By.XPATH, "//a[contains(text(),'История заказов')]"
    BUTTON_LOG_OUT = By.XPATH, "//button[contains(text(),'Выход')]"
    ORDER = By.XPATH, "//p[contains(@class, 'text_type_digits-default')]"