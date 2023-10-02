import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def configure_browser():
    #browser.config.window_width = 1920 #800
    #browser.config.window_height = 1080 #900
    browser.config.driver.maximize_window()
    #browser.config.click_by_js = True
    #browser.config.wait_for_no_overlap_found_by_js = True
    browser.config.base_url = "https://demoqa.com"
    browser.config.timeout = 6.0

    yield

    browser.quit()
