from selene.core import command
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
import os.path

from model.data.users import Student
from utils.resource_handler import path


class Registration:
    def __init__(self):
        pass

    def open(self):
        browser.open("/automation-practice-form")

    def register(self, student: Student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.all('.custom-control-label').element_by(have.text(student.gender.value)).click()

        browser.element('#userNumber').type(student.mobile_phone)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(str(student.birthdate.year))).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(student.birthdate.strftime('%B'))).click()
        #browser.element(f'.react-datepicker__month-select>option[value=\'{str(user.birthdate.month)}\']').click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(str(student.birthdate.day))).click()

        browser.element('#subjectsInput').type(student.subject).press_enter()
        browser.all('.custom-control-label').element_by(have.text(student.hobbies.value)).click()
        browser.element('#uploadPicture').send_keys(path('tests/img/'+student.picture_path))
        browser.element('#currentAddress').type(student.current_address)
        browser.element('#state').click().element(by.text(student.state)).click()
        browser.element('#city').click().element(by.text(student.city)).click()

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').submit()

    def should_have_registered(self, user: Student):
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
