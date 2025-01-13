import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.reset_password_page import ResetPasswordPage
from config import FORGOT_PASS_PAGE, RESET_PASS_PAGE

class TestPasswordRecovery:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_recover_password_button_successful(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        current_url = login_page.click_on_button_password_recovery()
        assert current_url == FORGOT_PASS_PAGE

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_button_recover(self, driver, create_user_and_get_creds):
        user_data = create_user_and_get_creds[0]
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.click_on_button_password_recovery()
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.input_email(user_data)
        current_url = password_recovery.click_on_button_recovery(RESET_PASS_PAGE)
        assert current_url == RESET_PASS_PAGE

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_on_eye_button(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        login_page.click_on_button_password_recovery()
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.input_email(create_user_and_get_creds[0])
        password_recovery.click_on_button_recovery(RESET_PASS_PAGE)
        reset_password = ResetPasswordPage(driver)
        reset_password.click_on_eye_button()
        assert reset_password.is_password_visible