import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from termcolor import cprint
import time
import math

urls=[
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    cprint("\nstart browser for test..",'yellow')
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('siteurls',urls )
def test_guest_should_see_login_link(browser, siteurls):
    browser.implicitly_wait(5) #Ожидание появления  полей которые ищутся методом browser.find_element_by........
    browser.get(siteurls)
    #time.sleep(3)
    textarea=browser.find_element_by_xpath("//textarea")
    button = browser.find_element_by_xpath("//button[contains(@class,'submit-submission')]")
    answer = math.log(int(time.time()))
    textarea.send_keys(f"{answer}")
    #time.sleep(1)

    #button = browser.find_element_by_xpath("//button[contains(@class,'submit-submission')]")
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[not(@disabled) and contains(@class,'submit-submission')]"))) #Ожидание появления кнопули
    button.click()
    #time.sleep(3)
    result_text = browser.find_element_by_xpath("//pre")
    result_text = result_text.text

    assert "Correct!" == result_text, f"{siteurls} На данной странице результыты выполенния задания явно не Correct"
    #special for git
    print("Hi git")