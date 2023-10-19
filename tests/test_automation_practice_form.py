from datetime import date
from model.data.users import User, Gender, Hobbies
from model.pages.registration import Registration


def test_submit_form():
    registration = Registration()
    user = User(first_name='fname', last_name='lname', email='asd@asd.asd', gender=Gender.male,
                mobile_phone='0123456789', birthdate=date(1990, 8, 1), subject='Maths', hobbies=Hobbies.sports,
                picture_path='images.jpg', current_address='curr_adr', state='NCR', city='Delhi')
    registration.open()
    registration.register(user)
    registration.should_have_registered(user)
