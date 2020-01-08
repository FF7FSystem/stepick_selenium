from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time

@pytest.mark.need_review
@pytest.mark.parametrize('link', [
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_basket_link()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.confirm_add_book_name()
    page.confirm_add_book_price()
    page.confirm_add_book_name__param()
    page.confirm_add_book_price_param()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_basket_link()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_basket_link()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)   #чтобы увидеть что мы перешли на страницу логина

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link_in_head()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url) #при переходе на другую страницу, чтобы работать с методами
    # описанными ДЛЯ ЭТОЙ СТРАНИЦЫ (в отдельм файле\модуле), необходимо сделать на них ссылку, иначе методы будут искаться в приведущем
    # классе (тут это ProductPage)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        login_link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, login_link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        acc={'email':str(time.time()) + "@fakemail.org", 'password':'QAZwsxEDCrfvTGByhn'}
        page.register_new_user(**acc)
        page.should_be_authorized_user()
        time.sleep(2)
        self.link = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        page = ProductPage(browser,self.link)    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                              # открываем страницу
        page.should_be_basket_link()             #проверка наличия на страници кнопки "добавить в корзину"
        page.add_to_basket()
        page.confirm_add_book_name()            #проверка соответствия названия добавленной в корзину книги с заголовком книги
        page.confirm_add_book_price()           #та же проверка но цены

    def test_user_cant_see_success_message(self,browser):
        page = ProductPage(browser, self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                             # открываем страницу
        page.should_not_be_success_message()    #Прверка, что на странице отсутствует сообщения  о добалении в корзину
