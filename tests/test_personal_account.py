import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from config import PERSONAL_ACCOUNT_PAGE, ORDER_HISTORY_PAGE, LOGIN_PAGE

class TestPersonalAccount:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_transfer_to_personal_account(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        current_url = main_page.click_on_personal_account_button()
        assert current_url == PERSONAL_ACCOUNT_PAGE

    @allure.title('переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.click_on_personal_account_button()
        personal_account = PersonalAccountPage(driver)
        current_url = personal_account.click_on_order_history()
        assert current_url == ORDER_HISTORY_PAGE

    @allure.title('выход из аккаунта')
    def test_log_out_of_account(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.input_email_and_password(create_user_and_get_creds)
        login_page.click_on_login_button()
        main_page.wait_page_to_be_loaded()
        main_page.click_on_personal_account_button()
        personal_account = PersonalAccountPage(driver)
        current_url = personal_account.click_on_log_out_from_acc()
        assert current_url == LOGIN_PAGE