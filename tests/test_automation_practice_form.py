from selene import have
from model.pages.registration import Registration


def test_submit_form():
    registration = Registration()
    registration.open()

    registration.set_first_name('fName')
    registration.set_last_name('lName')
    registration.set_email('asd@asd.as')
    registration.set_gender('Male')
    registration.set_phone_number('0123456789')
    registration.set_birthdate('1999', 'August', '8')
    registration.set_subject('Maths')
    registration.set_hobbie('Sports')

    registration.upload_image('images.jpg')
    registration.set_current_address('currentAddr')
    registration.set_state('NCR')
    registration.set_city('Delhi')
    registration.submit_form()

    registration.modal_header_should_have('Thanks for submitting the form')

    registration.confirmation_table_should_have('fName lName',
                   'asd@asd.as',
                   'Male',
                   '0123456789',
                   "08 August,1999",
                   'Maths',
                   'Sports',
                   'images.jpg',
                   'currentAddr',
                   'NCR Delhi')
