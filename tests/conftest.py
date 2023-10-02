import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def configure_browser():
    browser.config.driver.maximize_window()
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 6.0

    yield

    browser.quit()
