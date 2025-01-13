from selenium.webdriver.common.by import By

class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"
    MAIN_PAGE_HEADER = By.XPATH, "//h1[contains(text(),'Соберите бургер')]"
    BUTTON_CREATE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(),'Конструктор')]"
    ORDER_FEED_BUTTON = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    INGREDIENT = By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]"
    BASKET = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    TITLE_MODAL_INGREDIENT = By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"
    ORDER_MODAL_WINDOW = By.XPATH, "//p[text()='идентификатор заказа']"
    CLOSE_MODAL_ORDER_WINDOW_BUTTON = By.XPATH, "//button[@type='button']"
    MODAL_ELEMENT = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"
    CLOSE_MODAL_WINDOW = By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button"
    COUNTER_INGREDIENT = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class,'Modal_modal__title')]"