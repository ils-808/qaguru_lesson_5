from selene.core import command
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
import os.path

class Registration:
    def __init__(self):
        pass

    def open(self):
        browser.open("/automation-practice-form")
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')

    def set_first_name(self, value):
        browser.element('#firstName').type(value)

    def set_last_name(self, value):
        browser.element('#lastName').type(value)

    def set_email(self, value):
        browser.element('#userEmail').type(value)

    def set_gender(self, value):
        browser.all('.custom-control-label').element_by(have.text(value)).click()

    def set_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def set_birthdate(self, year, month, date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(year)).click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(month)).click()
        browser.all('.react-datepicker__day').element_by(have.text(date)).click()

    def set_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def set_hobbie(self, value):
        browser.all('.custom-control-label').element_by(have.text(value)).click()

    def upload_image(self, file_name):
        browser.element('#uploadPicture').send_keys(os.path.abspath(file_name))

    def set_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def set_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def set_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').submit()

    def get_modal_header(self):
        return browser.element('.modal-header')

    def get_confirmation_table(self):
        return browser.element('.table')
