import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.title('Клик по кнопке войти')
    def click_on_login_button(self):
        login_button = self.wait_for_element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.click_on_element_js(login_button)

    @allure.title('Ввод логина и пароля')
    def input_email_and_password(self, create_user_and_get_creds):
        # Проверяем, является ли create_user_and_get_creds кортежем с одним элементом
        if isinstance(create_user_and_get_creds, tuple):
            user_data = create_user_and_get_creds[0]  # Если кортеж, извлекаем первый элемент
        else:
            user_data = create_user_and_get_creds  # Если словарь, то сразу берем его

        email = user_data['email']
        password = user_data['password']

        email_input = self.find_element_with_wait(LoginPageLocators.INPUT_NAME)
        password_input = self.find_element_with_wait(LoginPageLocators.INPUT_PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)

    @allure.title('Клик на кнопку "Восстановить пароль"')
    def click_on_button_password_recovery(self):
        recovery_button = self.find_element_with_wait(LoginPageLocators.PASSWORD_RECOVERY)
        self.click_on_element_js(recovery_button)
        current_url = self.current_url()
        return current_url