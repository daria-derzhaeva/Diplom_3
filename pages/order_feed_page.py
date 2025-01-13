import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from config import MAIN_PAGE

class OrderFeedPage(BasePage):

    @allure.title('Клик на кнопку "Конструктор"')
    def click_on_button_constructor(self):
        button_constructor = self.find_element_with_wait(OrderFeedLocators.BUTTON_CONSTRUCTOR)
        self.click_on_element_js(button_constructor)
        self.wait_url_to_be(MAIN_PAGE)
        return self.current_url()

    @allure.title('Клик на заказ')
    def click_on_order(self):
        order = self.find_element_with_wait(OrderFeedLocators.ORDER)
        self.click_on_element_js(order)

    @allure.title('Проверка видимости окна создания заказа')
    def order_window_is_visible(self):
        title_modal_window = self.find_element_with_wait(OrderFeedLocators.ORDER_MODAL_WINDOW)
        return title_modal_window.is_displayed()

    @allure.title('Проверка наличия номера заказа в списке всех заказов')
    def order_number_in_list(self, order_number):
        order_element = self.find_elements_with_wait(OrderFeedLocators.ORDER_FEED_LIST)

        for _ in order_element:
            order_element_text = self.get_text_from_element(OrderFeedLocators.ORDER_LIST_NUMBERS)
            if order_element_text == order_number:
                return True
            return False


    @allure.title('Получение номера счетчика выполненных заказов за все время')
    def get_all_time_counter_number(self):
        self.find_element_with_wait(OrderFeedLocators.ALL_TIME_COUNTER)
        all_time_counter = self.get_text_from_element(OrderFeedLocators.ALL_TIME_COUNTER)
        return all_time_counter

    @allure.step("Проверка увеличения счетчика выполненных заказов за все время")
    def is_all_time_counter_increased(self, initial_counter):
        current_counter = self.get_all_time_counter_number()
        return int(current_counter) > int(initial_counter)

    @allure.step("Получение номера счетчика выполненных заказов за сегодня")
    def get_today_counter_number(self):
        self.find_element_with_wait(OrderFeedLocators.TODAY_COUNTER)
        today_counter = self.get_text_from_element(OrderFeedLocators.TODAY_COUNTER)
        return today_counter

    @allure.step("Проверка увеличения счетчика выполненных заказов за сегодня")
    def today_counter_increased(self, initial_counter):
        current_counter = self.get_today_counter_number()
        return int(current_counter) > int(initial_counter)

    @allure.step("Ожидание появления заказа в списке заказов 'В работе'")
    def wait_for_order_to_appear(self, order_number):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.is_order_number_in_work_list(order_number)
        )
        return True

    @allure.step("Проверка наличия номера заказа в списке 'В работе'")
    def is_order_number_in_work_list(self, order_number):
        orders_section = self.find_elements_with_wait(OrderFeedLocators.IN_WORK_ORDERS)

        for order in orders_section:
            order_text = order.text[1:]
            if order_text == order_number:
                return True
        return False