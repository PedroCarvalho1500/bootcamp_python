import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException



class MainPage:
    #constructor
    def __init__(self,driver):
        self.driver=driver
        #Locators
        self.register_button_xpath = '//div[@class="navbar-right hidden-xs"]/a[contains(text(),"Register")]'
        self.register_label_xpath = '//h3[contains(text(),"Register for OpenCart account")]'

        #WAIT ELEMENTS
        self.mywait=WebDriverWait(self.driver,30,poll_frequency=3,ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException,
                                                        Exception]
                            )


    def wait_element_by(self,locator_type, locator):
        if(locator_type == "CSS"): return self.mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,locator)))
        else: return self.mywait.until(EC.presence_of_element_located((By.XPATH,locator)))

    #action methods
    def open_register_page(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()

        try:
            while(self.driver.find_element(By.XPATH, '//div[contains(text(),"www.opencart.com needs to review the security of your connection before proceeding.")]').is_displayed() == True):
                time.sleep(1)
                self.driver.add_cookie({'name':'_ga_X8G0BRFSDF', 'value':'GS1.1.1690985575.1.1.1690987933.0.0.0'})
                self.driver.add_cookie({'name':'PHPSESSID', 'value':'5ab30e1b094273ad8497432510'})
                self.driver.add_cookie({'name':'ts', 'value':'vreXpYrS%3D1778867940%26vteXpYrS%3D1684261740%26vr%3D25b727ea1880a6242ae5c34bfecd352f%26vt%3D25b727ea1880a6242ae5c34bfecd352e'})
                self.driver.add_cookie({'name':'ts_c', 'value':'vr%3D25b727ea1880a6242ae5c34bfecd352f%26vt%3D25b727ea1880a6242ae5c34bfecd352e'})
                self.driver.add_cookie({'name':'currency', 'value':'USD'})
                self.driver.add_cookie({'name':'enforce_policy', 'value':'ccpa'})
                self.driver.add_cookie({'name':'cf_clearance', 'value':'zytArTE54GcxOLsqOr5ZxBswEQ.rRQwzaYQnP3WtUlw-1690985574-0-1-31ad99bb.30112e4a.66acc65b-150.2.1690985574'})
                self.driver.add_cookie({'name':'_gid', 'value':'GA1.2.215543229.1690985576'})
                #self.driver.add_cookie({'name':'_gat_gtag_UA_1988725_1', 'value':1})
                
                self.driver.add_cookie({'name':'_ga', 'value':'GA1.2.794314339.1690985575'})

                #input("SKIP...")
        except:
            print()
        self.wait_element_by("XPATH", self.register_label_xpath)