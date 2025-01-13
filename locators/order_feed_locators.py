from selenium.webdriver.common.by import By

class OrderFeedLocators:

    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"
    ORDER = By.XPATH, "//p[contains(@class, 'text_type_digits-default')]"
    ORDER_MODAL_WINDOW = By.XPATH, "//div[contains(@class,'Modal_orderBox__1xWdi')]"
    ORDER_FEED_LIST = By.CSS_SELECTOR, ".OrderFeed_list__OLh59 > li"
    ORDER_LIST_NUMBERS = By.CSS_SELECTOR, '.text.text_type_digits-default'
    ALL_TIME_COUNTER = By.XPATH, "//div[p[text()='Выполнено за все время:']]/p[2]"
    TODAY_COUNTER = By.XPATH, "//div[p[text()='Выполнено за сегодня:']]/p[2]"
    IN_WORK_ORDERS = By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li"