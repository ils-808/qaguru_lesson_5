from typing import Literal

import pytest
import selene
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene import browser, Browser, Config
import os
import pydantic_settings

from utils import attach
from utils.resource_handler import path

BrowserType = Literal['chrome', 'firefox', 'edge']


class Configure(pydantic_settings.BaseSettings):
    context: Literal['local', 'prod'] = 'prod'
    base_url: str = 'https://demoqa.com'
    height: str = '1080'
    width: str = '1920'
    timeout: float = 3.0
    browser: BrowserType = 'chrome'
    version: str = '100'

config = Configure(_env_file=path(f'.env.{Configure().context}'))

@pytest.fixture(scope='function', autouse=True)
def configure_browser():

    options = Options()
    selenoid_capabilities = {
        'browserName': config.browser,
        'browserVersion': config.version,
        #'screenResolution': '(1920x1080x24)',#f'({config.width}*{config.height})',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    options.add_argument(f'--window-size={config.width},{config.height}')
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.window_width
    browser.config.base_url = config.base_url
    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    #attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
