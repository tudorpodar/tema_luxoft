from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
	locator = "q"

class GoButtonElement(BasePageElement):
	locator = "submit"

class Basepage(object):
	def __init__(self,driver):
		self.driver = driver


class MainPage(Basepage):

	search_text_element = SearchTextElement()
	def is_title_matches(self):
		return "Python" in self.driver.title

	def click_go_button(self):
		element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
		element.click()

	def hover_download_menu(self):
		element = self.driver.find_element(*MainPageLocators.hover_download)
		hover = ActionChains(self.driver).move_to_element(element)
		hover.perform()

class SearchResultPage(Basepage):

	def is_results_found(self):
		return "No results found." not in self.driver.page_source

	def click_PEP_link(self):
		element = self.driver.find_element(*SearchResultsPageLocators.click_PEP_link)
		element.click()

class ExamplesResultPage(Basepage):

	def click_examples_link(self):
		element = self.driver.find_element(*ExamplePageLocators.click_examples_link)
		element.click()

	def examples_number(self):
		element = self.driver.find_element(*ExamplePageLocators.click_examples_link)
		element.click()