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

    registration.upload_image('img/images.jpg')
    registration.set_current_address('currentAddr')
    registration.set_state('NCR')
    registration.set_city('Delhi')
    registration.submit_form()

    registration.get_modal_header().should(have.text('Thanks for submitting the form'))
    registration.get_confirmation_table().all('td:nth-child(2)').should(
        have.texts('fName lName',
                   'asd@asd.as',
                   'Male',
                   '0123456789',
                   "08 August,1999",
                   'Maths',
                   'Sports',
                   'images.jpg',
                   'currentAddr',
                   'NCR Delhi'))
