import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_open():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open('https://google.com')

    yield browser

    browser.quit()
