from typing import Literal

import pytest
from selene import browser
import os
import pydantic_settings
from utils.resource_handler import path

BrowserType = Literal['chrome', 'firefox', 'edge']


class Config(pydantic_settings.BaseSettings):
    context: Literal['local', 'prod'] = 'local'
    base_url: str = 'https://demoqa.com'
    height: int = 800
    width: int = 1000
    timeout: float = 3.0
    browser: BrowserType = 'firefox'


config = Config(_env_file=path(f'.env.{Config().context}'))

@pytest.fixture(scope='function', autouse=True)
def configure_browser():
    browser.config.driver_name = config.browser
    browser.config.window_width = config.width #os.getenv('width',  1920)
    browser.config.window_height = config.height #os.getenv('height', 1680)
    browser.config.base_url = config.base_url #os.getenv('base_url', "https://demoqa.com")
    browser.config.timeout = config.timeout #6.0

    yield

    browser.quit()
