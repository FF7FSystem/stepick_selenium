from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.LINK_OF_ITEMS), "Basket is not empty"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESS_BASKET_EMPTY), "Empty basket message is not presented, but should be"



