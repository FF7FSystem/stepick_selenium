import unittest
from selenium import webdriver
import time


def registration(link):

    browser = webdriver.Chrome()
    browser.get(link)s

    input1 = browser.find_element_by_xpath("//label[contains(text(),'First name')]/following-sibling::input")
    input1.send_keys("Ivan")
    input1 = browser.find_element_by_xpath("//label[contains(text(),'Last name')]/following-sibling::input")
    input1.send_keys("Ivanov")
    input1 = browser.find_element_by_xpath("//label[contains(text(),'Email')]/following-sibling::input")
    input1.send_keys("Ivan@gmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    return welcome_text_elt.text


class TestRegistration1(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "Проверка заполнения обязательных полей формы регистриции с сылкой №1")

    def test_registration2(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "Проверка заполнения обязательных полей формы регистриции с сылкой №2")


if __name__ == "__main__":
    unittest.main()