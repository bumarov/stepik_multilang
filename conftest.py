from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru",
                     help="Choose language")


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
