from .base_page import BasePage
from .locators import BasketPageLocators,ProductPageLocators


class ProductPage(BasePage):

    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), "Basket link is not presented"

    def add_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def confirm_add_book_name(self):
        assert self.is_element_present(*BasketPageLocators.CONFIRM_BOOK_NAME), "the name of the book added in basket does not match"

    def confirm_add_book_price(self):
        assert self.is_element_present(*BasketPageLocators.CONFIRM_BOOK_PRICE), "the price of the book added in basket does not match"

    def search_book_name(self):
        name_link = self.browser.find_element(*BasketPageLocators.BOOK_NAME)
        return  name_link.text

    def search_book_price(self):
        price_link = self.browser.find_element(*BasketPageLocators.BOOK_PRICE)
        return  price_link.text

    def confirm_add_book_name__param(self):
        name=self.search_book_name()
        assert self.browser.find_element_by_xpath(f"//strong[text()='{name}']"), "the name of the book added in basket does not match _ 2"

    def confirm_add_book_price_param(self):
        price_in_title = self.search_book_price()
        try:
            price_in_basket = self.browser.find_element_by_xpath("//div[contains(@class,'basket-mini')]").text
            price_in_basket = price_in_basket.strip()
        except:
            print('По указанном Хратн ничего не найдено или неверный Хпатн')
            price_in_basket=""
        assert price_in_title in price_in_basket , f"the price of the book added in basket does not match _2, {price_in_title},  {price_in_basket}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, and it shouldn't"

