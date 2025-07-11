import pytest
from base import BaseTest
import time


class Test_Page(BaseTest):
    def setUp(self):
        url = "https://www.houseofindya.com/"
        self.driver = self.setUpDriver()
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.smoke
    def test_method_name(self):
        # Write your methods here
        
        kids = self.driver.find_element(By)
        kids.click()

        self.driver.refresh()
        time.sleep

        locator = self.driver.find_element(By)
        locator.click()

        self.driver.refresh()
        time.sleep(2)
# //a[@href='/women-lehenga-set/cat'][normalize-space()='Lehengas']
        Lehengas = self.driver.find_element(By.CSS_SELECTOR, "a[href='/menswear']")
        Lehengas.click()

        time.sleep(2)

