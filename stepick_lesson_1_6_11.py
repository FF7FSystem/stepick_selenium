
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html" #Рабочая форма
    link2 = "http://suninjuly.github.io/registration2.html" # Форма с Багом (нет обязательного поля Last name)
    browser = webdriver.Chrome()
    browser.get(link2)

     #Поиск по Xpath, ищет поле формы в названии которого есть необходимая подстрока и выбирает от него следующий сестринский тег инпут.
    input1 = browser.find_element_by_xpath("//label[contains(text(),'First name')]/following-sibling::input")
    input1.send_keys("Ivan")
    input1 = browser.find_element_by_xpath("//label[contains(text(),'Last name')]/following-sibling::input")
    input1.send_keys("Ivanov")
    input1 = browser.find_element_by_xpath("//label[contains(text(),'Email')]/following-sibling::input")
    input1.send_keys("Ivan@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()