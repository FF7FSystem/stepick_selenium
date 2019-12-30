import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    #Все для тебя Юзер, удали решетку и проверяй на здоровье, 5 секунд вполне достаточно чтобы увидить язык
    #time.sleep(5)
    assert browser.find_element_by_xpath("//button[contains(@class,'add-to-basket')]")