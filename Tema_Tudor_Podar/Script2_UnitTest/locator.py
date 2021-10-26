from selenium.webdriver.common.by import By

class MainPageLocators(object):
	GO_BUTTON = (By.ID, "submit")
	hover_download = (By.LINK_TEXT, "Downloads")

class SearchResultsPageLocators(object):
	click_PEP_link = (By.LINK_TEXT, "PEP 318 -- Decorators for Functions and Methods")

class ExamplePageLocators(object):
	click_examples_link = (By.ID, "id80")
	examples_section = (By.ID,"examples")