import time
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_xpath("//button[@value='Добавить в корзину']")