import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_width = 1400
    browser.config.window_height = 700


