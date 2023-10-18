from selene.support.shared import browser

from model.components.panel import Panel
from model.pages.registration import Registration
from model.pages.simple_registration import SimpleRegistration


class Application:
    def __init__(self):
        self.registration = Registration()
        self.simple_registration = SimpleRegistration()
        self.panel = Panel()

    @property
    def remove_bottom_elements(self):
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')


app = Application()
