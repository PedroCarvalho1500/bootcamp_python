import pytest
import json
from pageObjects.register_page import RegisterPage
from testCases.teardown_conf import TeardownConf
from testCases.conftest import SetupConf
from pageObjects.main_page import *
from utilities.random_string import random_string_generator

class TestRegister(SetupConf,TeardownConf):
    def testSuccessfullyRegisteredWithMandatoryFields(self, teardown):
        print("Success: Register only filling mandatory fields")
        self.givenConfig("Chrome")
        #input("HERE...")
        #self.driver.execute_script("window.localStorage.setItem('{}', {})".format('__paypal_storage__', json.dumps('{"id":"uid_1a761fcfcb_mtq6mti6ntu","__session__":{"guid":"uid_17e112ae1d_mtq6mti6ntu","created":1690985575521}}')))

        self.main_page = MainPage(self.driver)
        self.main_page.open_register_page()

        self.register_page = RegisterPage(self.driver)

        random_string = random_string_generator()
        self.register_page.fill_username_field(random_string)
        self.register_page.fill_firstName_field(random_string)
        self.register_page.fill_lastName_field(random_string)
        self.register_page.fill_email_field(random_string+"@email.com")
        self.register_page.select_country_field('Brazil')
        self.register_page.fill_password_field(random_string+"&!#$")
        self.register_page.click_on_correct_icon()
        self.register_page.click_on_register()
        input()
        assert 1 == 1