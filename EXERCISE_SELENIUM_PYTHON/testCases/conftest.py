import time
import pytest

from utilities.config import BASE_URL, VALID_PASSWORD, VALID_USERNAME, beforeChrome, beforeFirefox


givenConfigDict = {
    "Chrome": lambda: beforeChrome(),
    "Firefox": lambda: beforeFirefox()
}


class SetupConf():

    def givenConfig(self, browser):
        self.driver = givenConfigDict[browser]() 

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)