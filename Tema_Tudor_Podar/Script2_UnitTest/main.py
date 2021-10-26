import unittest
from selenium import webdriver
import page
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		print("setup")
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
		self.driver.get("https://www.python.org/")
		time.sleep(5)

	def test_search_python(self):
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()
		mainPage.search_text_element = "decorator"
		mainPage.click_go_button()
		search_result_page = page.SearchResultPage(self.driver)
		assert search_result_page.is_results_found()
		time.sleep(5)
		
		searchPage = page.SearchResultPage(self.driver)
		searchPage.click_PEP_link()

		time.sleep(5)

		examplePage = page.ExamplesResultPage(self.driver)
		examplePage.click_examples_link()

		time.sleep(5)

		try:
			example_section = WebDriverWait(self.driver, 10). until(
			EC.presence_of_element_located((By.ID,"examples"))
			)

			examples = example_section.find_elements_by_class_name("first")
			print("Numarul de exemple este:",len(examples))

	

		finally:
			self.driver.quit()




	# def test_example(self):
	# 	print("Test")
	# 	assert True

	# def tearDown(self):
	# 	# self.driver.close()


if __name__=="__main__":
	unittest.main()