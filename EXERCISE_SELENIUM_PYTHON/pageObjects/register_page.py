import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.select import Select


class RegisterPage:
    #constructor
    def __init__(self,driver):
        self.driver=driver
        #Locators
        self.username_field_css = 'input[id="input-username"]'
        self.firstName_field_css = 'input[id="input-firstname"]'
        self.lastName_field_css = 'input[id="input-lastname"]'
        self.email_field_css = 'input[id="input-email"]'
        self.country_field_css = 'select[id="input-country"]'
        self.password_field_css = 'input[id="input-password"]'
        #ddelement.select_by_value('1')
        self.register_button_xpath = '//button[contains(text(),"Register")][1]'
        self.icons_list_xpath = '//ul[@class="list-inline"]/li/a'
        self.successfull_selected_icon_xpath = '//div[contains(text()," Success: You passed!")]'


        #WAIT ELEMENTS
        self.mywait=WebDriverWait(self.driver,30,poll_frequency=3,ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException,
                                                        Exception]
                            )


    def wait_element_by(self,locator_type, locator):
        if(locator_type == "CSS"): return self.mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,locator)))
        else: return self.mywait.until(EC.presence_of_element_located((By.XPATH,locator)))

    def fill_username_field(self,value):
        self.driver.find_element(By.CSS_SELECTOR,self.username_field_css).send_keys(value)

    def fill_firstName_field(self,value):
        self.driver.find_element(By.CSS_SELECTOR,self.firstName_field_css).send_keys(value)

    def fill_lastName_field(self,value):
        self.driver.find_element(By.CSS_SELECTOR,self.lastName_field_css).send_keys(value)

    def fill_email_field(self,value):
        self.driver.find_element(By.CSS_SELECTOR,self.email_field_css).send_keys(value)

    def select_country_field(self,value):
        ddelement= Select(self.driver.find_element(By.CSS_SELECTOR,self.country_field_css))
        ddelement.select_by_visible_text(value)

    def fill_password_field(self,value):
        self.driver.find_element(By.CSS_SELECTOR,self.password_field_css).send_keys(value)

    def click_on_correct_icon(self):
        successfull_appear = False
        while(successfull_appear == False):
            icons = self.driver.find_elements(By.XPATH, self.icons_list_xpath)
            index = random.randint(0, len(icons) - 1)
            icons[index].click()
            try:
                successfull_appear = self.driver.find_element(By.XPATH,self.successfull_selected_icon_xpath).is_displayed()
            except:
                successfull_appear = False
            #input("ATTEMPT")


    def click_on_register(self):
        self.driver.find_element(By.XPATH,self.register_button_xpath).click()


    #action methods
