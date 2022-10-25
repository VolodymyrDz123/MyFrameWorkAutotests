import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    chrome_service = Service(executable_path="./chromedriver")
    browser = webdriver.Chrome(service=chrome_service)
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru or en")
