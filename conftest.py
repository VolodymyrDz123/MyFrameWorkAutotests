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

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")
