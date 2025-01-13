import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators

class ResetPasswordPage(BasePage):

    def input_password(self, create_user_and_get_creds):
        email = create_user_and_get_creds['email']
        email_input = self.find_element_with_wait(ResetPasswordLocators.RESET_PASSWORD_INPUT)
        email_input.send_keys(email)

    def click_on_eye_button(self):
        eye_button = self.find_element_with_wait(ResetPasswordLocators.EYE_BUTTON)
        self.click_on_element_js(eye_button)

    @allure.step("Проверка видимости пароля")
    def is_password_visible(self):
        password_input = self.find_element_with_wait(ResetPasswordLocators.RESET_PASSWORD_INPUT)
        return password_input.get_attribute('type') == 'text'
