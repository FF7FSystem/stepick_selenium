import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
"""сonftest.py  в этот файл выносятся фиктуры для тестов, чтобы не плодить их в каждом тестовом файле"""


def pytest_addoption(parser):
    """
    Функция считывания перменной language из командной строки
    :param parser: определение настроек считывания с командной строки
    :return: Ничего не возвращает, является преднастройкой, чтобы с коммандной строки можно было стчитывать
    """
    parser.addoption('--language', action='store', default='en', help="language: ru or en or es or ...")

@pytest.fixture(scope="function")
def browser(request):
    """
    Фиктура, подготавливает браузер к запуску теста. В данном случае так же
    считывается значения языка, для передачи в браузер и отображения страницы на этом языке
    :param request:
    :return:
    """
    language = request.config.getoption("language") #Получение значения переменной из командной строки
    browser = None

    if language:
        options = Options()                                                            #Настройка заголовка для передачи в бразер
        options.add_experimental_option('prefs', {'intl.accept_languages': language})  #Настройка заголовка для передачи в бразер
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)                                    #Вызов браузера с настройками
    else:
        raise pytest.UsageError("Dont select language (ru,en,es, ...)")                #Поднять исключение если язык не был указан в командной строке
    yield browser
    print("\nquit browser..")
    browser.quit()