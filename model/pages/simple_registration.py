from selene import query
from selene.support.conditions import have
from selene.support.shared import browser

from model.data.users import User


class SimpleRegistration:

    def open(self):
        browser.open('/text-box')

    def register_user(self, user : User):
        browser.element('#userName').type(user.full_name)
        browser.element('#userEmail').type(user.email)
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#permanentAddress').type(user.perm_address)
        browser.element('#submit').click()

    def should_be_registred(self, user: User):
        browser.all('#output p').should(have.texts(
            f'Name:{user.full_name}',
            f'Email:{user.email}',
            f'Current Address :{user.current_address}',
            f'Permananet Address :{user.perm_address}'
        ))
