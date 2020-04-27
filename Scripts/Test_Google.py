import sys,unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LendingFrontSearch(unittest.TestCase):

    def setUp(lending):
        lending.driver = webdriver.Chrome(executable_path=r"..\chromedriver.exe")

    def test_search_keyword_assert(lending):
        driver = lending.driver
        driver.get("https://www.google.com/")
        elem = driver.find_element_by_name("q")
        keyword = "1T2e3s4t5E6x7a8m9p0l1e2P3y4t5h6o7n8L9e0n1d2i3n4g5F6r7o8n9t0"
        elem.send_keys(keyword)
        elem.send_keys(Keys.RETURN)
        assert "No se han encontrado resultados para tu búsqueda" not in driver.page_source, "No se han encontrado resultados de la palabra " + keyword


    def tearDown(lending):
        lending.driver.close()

if __name__ == "__main__":
    unittest.main()