import pytest
from selene import browser


@pytest.fixture()
def browser_open():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open('https://google.com')

    yield

    # print("1111111")
