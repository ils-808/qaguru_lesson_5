from selene.support.conditions import have
from selene.support.shared import browser


class Panel:
    def __init__(self):
        self.container = browser.all('.header-wrapper .header-text')

    def open_simple_registration_form(self):
        self.open(element='Elements', item='Text Box')

    def open(self, element, item):
        browser.open('/automation-practice-form')
        self.container.element_by(have.exact_text(element)).click()
        browser.all('.left-pannel .btn-light[id^=item]>span').element_by(have.text(item)).click()
        self.remove_bottom_elements()

    def remove_bottom_elements(self):
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')