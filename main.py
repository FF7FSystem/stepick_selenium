import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")

wait_true_or_12sec = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
button = driver.find_element_by_xpath("//button[@id='book']")
button.click()

number1 = driver.find_element_by_id("input_value")
number1 = int(number1.text)

#print(browser.switch_to.window(window_name))
#time.sleep(5)

#button = driver.find_element_by_tag_name("button")
#driver.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()


#new_window = driver.window_handles[1]
#confirm = driver.switch_to.alert
#confirm.accept()
#print((new_window))
#driver.switch_to.window(new_window)
#number1 = driver.find_element_by_id("input_value")
#number = driver.find_element_by_xpath("//img/@valuex")
#number1 = number1.get_attribute("valuex")
#number1 = int(number1.text)

#number2 = driver.find_element_by_id("num2")
#number2 = int(number2.text)
result=calc(number1)
inp = driver.find_element_by_id("answer")
inp.send_keys(result)

#select = Select(driver.find_element_by_tag_name("select"))
#select.select_by_value(str(result)) # ищем элемент с текстом "Python"
#number = number.text
#result=calc(number)

#textarea = driver.find_element_by_id("answer")
#textarea.send_keys(result)

#checkbox = driver.find_element_by_id("robotCheckbox")
#checkbox.click()

#radio = driver.find_element_by_css_selector('label[for="robotsRule"]')
#radio = driver.find_element_by_id("robotsRule")
#radio.click()

#time.sleep(1)
# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера

driver.quit()

"""
find_element_by_id - поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
find_element_by_css_selector - поиск элемента с помощью правил на основе CSS.
find_element_by_xpath - поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
find_element_by_name - поиск по атрибуту name элемента;
find_element_by_tag_name - поиск элемента по названию тега элемента;
find_element_by_class_name - поиск по значению атрибута class;
find_element_by_link_text - поиск ссылки на странице по полному совпадению;
find_element_by_partial_link_text - поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылк
"""