import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage

class TestOrderFeedPage:

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_on_order_show_modal_window(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_order()
        order_modal_window_details = order_feed_page.order_window_is_visible()
        assert order_modal_window_details is True

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_display_in_feed_new_order_from_history(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.move_ingredient_to_order()
        main_page.click_on_button_create_order()
        main_page.close_order_window()
        main_page.click_on_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_order_history()
        created_order_number = personal_account_page.get_number_order_from_history_order()
        main_page.click_on_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_number_is_in_list = order_feed_page.order_number_in_list(created_order_number)
        assert order_number_is_in_list

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_order_increases_all_time_counter(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.click_on_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        initial_orders_amount = order_feed_page.get_all_time_counter_number()
        order_feed_page.click_on_button_constructor()
        main_page.move_ingredient_to_order()
        main_page.click_on_button_create_order()
        main_page.close_order_window()
        main_page.click_on_order_feed_button()
        all_time_counter_increased = order_feed_page.is_all_time_counter_increased(initial_orders_amount)
        assert all_time_counter_increased

    @allure.title('Создание заказа увеличивает счетчик заказов за сегодня')
    def test_creating_order_increases_day_counter(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.click_on_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        initial_orders_amount = order_feed_page.get_today_counter_number()
        order_feed_page.click_on_button_constructor()
        main_page.move_ingredient_to_order()
        main_page.click_on_button_create_order()
        main_page.close_order_window()
        main_page.click_on_order_feed_button()
        today_counter_increased = order_feed_page.today_counter_increased(initial_orders_amount)
        assert today_counter_increased

    @allure.title('Созданный заказ отображается в разделе "В работе"')
    def test_created_order_is_in_in_work_section(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.move_ingredient_to_order()
        main_page.click_on_button_create_order()
        created_order_number = main_page.get_order_number()
        main_page.close_order_window()
        main_page.click_on_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_order_to_appear(created_order_number)
        order_in_work = order_feed_page.is_order_number_in_work_list(created_order_number)
        assert order_in_work