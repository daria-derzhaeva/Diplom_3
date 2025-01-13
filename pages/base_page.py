from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def click_on_element_js(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    def current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )

    def move_elements(self, source, target):
        return drag_and_drop(self.driver, source, target)

    def wait_for_text_to_change(self, locator, initial_value):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_text_from_element(locator) != initial_value
        )