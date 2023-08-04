import pytest

from utilities.config import BASE_URL, VALID_PASSWORD, VALID_USERNAME, beforeChrome, beforeFirefox



class TeardownConf():
    
    @pytest.fixture()   # decorator
    def teardown(self):
        yield
        self.driver.quit()
        print("Closing browser..")
        


