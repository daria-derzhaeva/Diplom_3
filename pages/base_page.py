from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.default_timeout = default_timeout

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def click_on_element_js(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)

    def add_text_to_element(self, locator, text, timeout=None):
        self.find_element_with_wait(locator, timeout).send_keys(text)

    def get_text_from_element(self, locator, timeout=None):
        return self.find_element_with_wait(locator, timeout).text

    def wait_url_to_be(self, url, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def move_elements(self, source, target):
        return drag_and_drop(self.driver, source, target)

    def wait_for_text_to_change(self, locator, initial_value, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_text_from_element(locator) != initial_value
        )
