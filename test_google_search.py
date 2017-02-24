import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Ortnec")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        results = driver.find_elements_by_css_selector('div.g')
        link = results[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        #print(href)
        self.assertIn("http://ortnec.com/", href)


def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()