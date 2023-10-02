import os.path

from selene import browser, by, have, command


def test_submit_form():
    browser.open("/automation-practice-form")
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('footer').execute_script('element.remove()')

    browser.element('#firstName').type('fName')
    browser.element('#lastName').type('lName')
    browser.element('#userEmail').type('asd@asd.as')
    browser.all('.custom-control-label').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('August')).click() #.element_by(have.text('August')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1999')).click() #all('.react-datepicker__year-select').element_by(have.text('1991')).click()
    browser.all('.react-datepicker__day').element_by(have.text("8")).click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.all('.custom-control-label').element_by(have.text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/images.jpg'))
    browser.element('#currentAddress').type('currentAddr')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').submit()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(
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
