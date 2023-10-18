from datetime import date

from selene import have

from model.application_manager import app
from model.data.users import Student, Gender, Hobbies, User
from model.pages.registration import Registration


def test_submit_form():
    user = Student(first_name='fname', last_name='lname', email='asd@asd.asd', gender=Gender.male,
                   mobile_phone='0123456789', birthdate=date(1990, 8, 1), subject='Maths', hobbies=Hobbies.sports,
                   picture_path='images.jpg', current_address='curr_adr', state='NCR', city='Delhi')
    app.registration.open()
    app.remove_bottom_elements
    app.registration.register(user)
    app.registration.should_have_registered(user)


def test_simple_form():
    user = User(full_name='asd', email='asd@asd.asd', current_address='cur_addr', perm_address='perm_addr')
    app.panel.open_simple_registration_form('Elements', 'Text Box')
    app.remove_bottom_elements
    #app.simple_registration.open()
    app.simple_registration.register_user(user)
    app.simple_registration.should_be_registred(user)