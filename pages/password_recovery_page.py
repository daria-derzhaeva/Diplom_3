import allure
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):

    @allure.title('Клик по кнопке "восстановить"')
    def click_on_button_recovery(self, url):
        button_recovery = self.find_element_with_wait(PasswordRecoveryLocators.RESTORE_BUTTON)
        self.click_on_element_js(button_recovery)
        self.wait_url_to_be(url)
        current_url = self.current_url()
        return current_url

    def input_email(self, create_user_and_get_creds):
        email = create_user_and_get_creds['email']
        email_input = self.find_element_with_wait(PasswordRecoveryLocators.INPUT_EMAIL)
        email_input.send_keys(email)