import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config import PERSONAL_ACCOUNT_PAGE, ORDER_FEED_PAGE, MAIN_PAGE

class MainPage(BasePage):

    @allure.title('Клик на кнопку Войти в аккаунт')
    def click_on_login_button(self):
        login_button = self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON)
        self.click_on_element_js(login_button)

    def wait_page_to_be_loaded(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step("Клик на кнопку -> Личный кабинет")
    def click_on_personal_account_button(self):
        personal_account_button = self.find_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element_js(personal_account_button)
        self.wait_url_to_be(PERSONAL_ACCOUNT_PAGE)
        return self.current_url()

    @allure.title('Клик на кнопку конструктор')
    def click_on_constructor_button(self):
        constructor_button = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element_js(constructor_button)

    @allure.title('Клик на кнопку "лента заказов"')
    def click_on_order_feed_button(self):
        order_feed = self.find_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element_js(order_feed)
        self.wait_url_to_be(ORDER_FEED_PAGE)
        return self.current_url()

    @allure.title('клик на ингредиент Флюоресцентная булочка R2-D3')
    def click_on_ingredient(self):
        ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT)
        self.click_on_element_js(ingredient)

    @allure.title('Проверка видимости окна деталей ингредиент')
    def ingredient_details_window_is_visible(self):
        title_modal_window = self.find_element_with_wait(MainPageLocators.TITLE_MODAL_INGREDIENT)
        return title_modal_window.is_displayed()

    @allure.title('Закрытие модального окна после нажатия на крестик')
    def close_modal_window_ingredient(self):
        close_modal = self.find_element_with_wait(MainPageLocators.CLOSE_MODAL_WINDOW)
        self.click_on_element_js(close_modal)
        modal_element = self.find_element_with_wait(MainPageLocators.MODAL_ELEMENT)
        return 'Modal_modal_opened__3ISw4' not in modal_element.get_attribute('class')

    @allure.step("Перемещение ингредиента в корзину")
    def move_ingredient_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.INGREDIENT)
        target = self.find_element_with_wait(MainPageLocators.BASKET)
        self.move_elements(source, target)

    @allure.step("Проверка увеличения счетчика ингредиента")
    def is_ingredient_counter_increased(self):
        self.find_element_with_wait(MainPageLocators.COUNTER_INGREDIENT)
        counter_text = self.get_text_from_element(MainPageLocators.INGREDIENT)
        return counter_text != '0'

    @allure.title('клик на кнопку Оформить заказ')
    def click_on_button_create_order(self):
        create_order = self.find_element_with_wait(MainPageLocators.BUTTON_CREATE_ORDER)
        self.click_on_element_js(create_order)

    @allure.title('Проверка видимости окна создания заказа')
    def order_window_is_visible(self):
        title_modal_window = self.find_element_with_wait(MainPageLocators.ORDER_MODAL_WINDOW)
        return title_modal_window.is_displayed()

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        close_button = self.find_element_with_wait(MainPageLocators.CLOSE_MODAL_ORDER_WINDOW_BUTTON)
        self.click_on_element_js(close_button)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        initial_value = '9999'
        self.wait_for_text_to_change(MainPageLocators.ORDER_NUMBER, initial_value)
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)