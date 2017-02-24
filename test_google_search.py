import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleComSearch(unittest.TestCase):

    def setUp(self):
        """
        Creating Firefox WebDriver instance and setting implicitly wait up to 10 sec.
        :return:None
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_search_in_google_com(self):
        """

        :return:None
        """
        # Creating a local reference to the driver object created in setUp method
        driver = self.driver
        # Navigate to a google
        driver.get("http://www.google.com")
        # Confirming that title contains "Google"
        self.assertIn("Google", driver.title)
        print("Google is reached")
        # Looking for search field and searching for "Ortnec"
        elem = driver.find_element_by_name("q")
        elem.send_keys("Ortnec")
        elem.send_keys(Keys.RETURN)
        # Confirming that there are some results
        assert "No results found." not in driver.page_source
        # Looking for the top link in the search list
        results = driver.find_elements_by_css_selector('div.g')
        first_link = results[0].find_element_by_tag_name("a")
        href = first_link.get_attribute("href")
        # Confirming that the link is "http://ortnec.com/"
        self.assertIn("http://ortnec.com/", href)
        print("First link is {}".format(href))
        # Preparing the list of the URLs from the search results
        links = []
        for link in results:
            slink = link.find_element_by_tag_name("a")
            links.append(slink.get_attribute("href"))
        # Checking each link and each page contains "Ortnec" or "ortnec"
        for url in links:
            print("Looking for Ortnec in {}".format(url))
            driver.get(url)
            assert "Ortnec" in driver.page_source or "ortnec" in driver.page_source

    # Cleaning up
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()