from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    #LOGIN_LINK = (By.XPATH, "//a[@id='registration_link']/@href")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REG_FORM = (By.XPATH, "//form[@id='register_form']")

class BasketPageLocators():
    BASKET_LINK = (By.XPATH, "//button[contains(@class,'add-to-basket')]")
    BOOK_NAME = (By.XPATH, "//h1")
    CONFIRM_BOOK_NAME = (By.XPATH, "//strong[text()=//h1/text()]")
    BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
    CONFIRM_BOOK_PRICE = (By.XPATH, "//strong[contains(text(),//p[@class='price_color'])]")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, "//strong[text()='Deferred benefit offer']")

