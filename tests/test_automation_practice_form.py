from datetime import date

import allure
from selene import have

from model.application_manager import app
from model.data.users import Student, Gender, Hobbies, User
from model.pages.registration import Registration
import os


@allure.title('Регистрация полного пользователя')
def test_submit_form():
    user = Student(first_name='fname', last_name='lname', email='asd@asd.asd', gender=Gender.male,
                   mobile_phone='0123456789', birthdate=date(1990, 8, 1), subject='Maths', hobbies=Hobbies.sports,
                   picture_path='images.jpg', current_address='curr_adr', state='NCR', city='Delhi')
    with allure.step("Открыть форму регистрации"):
        app.registration.open()
    with allure.step("Удалить значения из футера"):
        app.remove_bottom_elements
    with allure.step("Выполнить попытку регистрации пользователя"):
        app.registration.register(user)
    with allure.step("Произвести проверку пользователя"):
        app.registration.should_have_registered(user)


@allure.title('Регистрация простого пользователя')
def test_simple_form():
    user = User(full_name='asd', email='asd@asd.asd', current_address='cur_addr', perm_address='perm_addr')
    with allure.step("Открыть форму регистрации"):
        app.panel.open_simple_registration_form()
    with allure.step("Выполнить попытку регистрации простого пользователя"):
        app.simple_registration.register_user(user)
    with allure.step("Произвести проверку пользователя"):
        app.simple_registration.should_be_registred(user)