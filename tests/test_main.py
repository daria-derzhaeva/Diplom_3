import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from config import MAIN_PAGE, ORDER_FEED_PAGE

class TestMainFunctionality:

    @allure.title('переход по клику на «Конструктор»')
    def test_transfer_on_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button()
        order_feed = OrderFeedPage(driver)
        current_url = order_feed.click_on_button_constructor()
        assert current_url == MAIN_PAGE

    @allure.title('переход на страницу "Лента заказов')
    def test_transfer_on_feed_order(self, driver):
        main_page = MainPage(driver)
        current_url = main_page.click_on_order_feed_button()
        assert current_url == ORDER_FEED_PAGE

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details = main_page.ingredient_details_window_is_visible()
        assert ingredient_details is True

    @allure.title('Модальное окно закрывается по нажатию на крестик')
    def test_close_modal_window_after_click_on_x(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        close_modal_details = main_page.close_modal_window_ingredient()
        assert close_modal_details is True

    @allure.title('Добавление ингредиента в корзину увеличивает счетчик ингредиента')
    def test_moving_ingredient_to_basket_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.move_ingredient_to_order()
        counter_increased = main_page.is_ingredient_counter_increased()
        assert counter_increased is True

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.move_ingredient_to_order()
        main_page.click_on_button_create_order()
        modal_window_order = main_page.order_window_is_visible()
        assert modal_window_order is True