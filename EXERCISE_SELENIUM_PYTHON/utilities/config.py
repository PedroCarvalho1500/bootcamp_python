from asyncio import exceptions
import json
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import csv

class Chrome:
    # Browser configuration for Chrome
    NAME = "chrome"
    EXECUTABLE_PATH = "../chromedriver"
    OPTIONS = [
        "--disable-extensions",
        "--disable-infobars",
        "--disable-popup-blocking",
        "--start-maximized",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--ignore-ssl-errors=yes",
        "--ignore-certificate-errors",
        "--headless",
    ]

class Firefox:
    # Browser configuration for Firefox
    NAME = "firefox"
    EXECUTABLE_PATH = "../geckodriver"
    OPTIONS = [
        "-headless",
    ]

# Application URL
BASE_URL = "http://www.opencart.com"

# User credentials
#VALID_USERNAME = str(os.environ.get("VALID_USERNAME"))
#VALID_PASSWORD = str(os.environ.get("VALID_PASSWORD"))
#INVALID_PASSWORD = str(os.environ.get("INVALID_PASSWORD"))


def beforeChrome():
    #chrome_options = Chrome()
    #print("REACH HERE")
    serv_obj = Service("chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.accept_insecure_certs = True
    #desired = ops.to_capabilities()
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    cookie = "PHPSESSID=5ab30e1b094273ad8497432510; currency=USD; cf_clearance=zytArTE54GcxOLsqOr5ZxBswEQ.rRQwzaYQnP3WtUlw-1690985574-0-1-31ad99bb.30112e4a.66acc65b-150.2.1690985574; _gid=GA1.2.215543229.1690985576; _gat_gtag_UA_1988725_1=1; _ga_X8G0BRFSDF=GS1.1.1690985575.1.1.1690985609.0.0.0; _ga=GA1.1.794314339.1690985575"
    #selenium_wire = {}
    #ops.add_argument("--headless")
    #ops.set_capability("loggingPrefs", {'performance': 'ALL', "profile.default_content_settings.popups": 1})
    #ops.add_argument("--proxy-bypass-list=*")
    ops.add_argument("--start-maximized")
    #ops.add_argument('--disable-gpu')
    #ops.add_argument('--disable-dev-shm-usage')
    #ops.add_argument('--no-sandbox')
    ops.add_argument(f'user-agent={user_agent}')
    ops.add_argument('--ignore-certificate-errors')
    #ops.add_argument("--proxy-server='direct://'")
    ops.add_argument('--disable-dev-shm-usage')
    ops.add_argument('--disable-extensions')
    ops.add_argument('--disable-popup-blocking')
    #ops.add_argument('--ignore-ssl-errors=yes')
    domain_1 = 'https://www.opencart.com'
    driver=webdriver.Chrome(service=serv_obj, options=ops)


    return driver


def beforeFirefox(): 
    serv_obj = Service("geckodriver.exe")
    ops=webdriver.FirefoxOptions()
    #ops.add_argument("--headless")
    #ops.set_capability("loggingPrefs", {'performance': 'ALL'})
    ops.add_argument("--proxy-bypass-list=*")
    ops.add_argument("--start-maximized")
    ops.add_argument('--disable-gpu')
    ops.add_argument('--disable-dev-shm-usage')
    ops.add_argument('--no-sandbox')
    ops.add_argument('--ignore-certificate-errors')
    ops.add_argument('--disable-popup-blocking')
    #ops.add_argument('--proxy-server=http://myproxy:port')

    driver = webdriver.Firefox(service=serv_obj, options=ops)

    return driver





