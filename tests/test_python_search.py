import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_google(self):
        self.driver.get("https://clouddeveloperapp.mybluemix.net")
        self.assertIn("Cloud Developer", self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

