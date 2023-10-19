from selene.core import command
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
import os.path

import tests
from model.data.users import User


class Registration:

    def open(self):
        browser.open("/automation-practice-form")
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('.custom-control-label').element_by(have.text(user.gender.value)).click()

        browser.element('#userNumber').type(user.mobile_phone)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(str(user.birthdate.year))).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(user.birthdate.strftime('%B'))).click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(str(user.birthdate.day))).click()

        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('.custom-control-label').element_by(have.text(user.hobbies.value)).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(\
            os.path.join(os.path.dirname(tests.__file__), f'img/{user.picture_path}')))
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#state').click().element(by.text(user.state)).click()
        browser.element('#city').click().element(by.text(user.city)).click()

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').submit()

    def should_have_registered(self, user: User):
        return browser.element('.table').all('td:nth-child(2)').should(
            have.texts(f'{user.first_name} {user.last_name}',
                       user.email,
                       user.gender.value,
                       user.mobile_phone,
                       user.birthdate.strftime("%d %B,%Y"),  # тут скорее всего будет ошибка. Формат даты
                       user.subject,
                       user.hobbies.value,
                       user.picture_path,
                       user.current_address,
                       f'{user.state} {user.city}'))
