from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_cart_button_exists(browser: WebDriver):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)

    try:
        cart_add_button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
        )
        assert cart_add_button != None
    except TimeoutException:
        assert False, "Button does not exist on the page."
