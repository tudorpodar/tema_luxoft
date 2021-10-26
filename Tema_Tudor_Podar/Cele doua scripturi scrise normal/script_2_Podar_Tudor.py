from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
# print(driver.title)

time.sleep(5)

search = driver.find_element_by_id("id-search-field")
search.send_keys("decorators")
# search.send_keys(Keys.RETURN)

time.sleep(2)

link = driver.find_element_by_id("submit")
link.click()

time.sleep(2)

# driver.get("https://www.python.org/dev/peps/pep-0318/")
link = driver.find_element_by_link_text("PEP 318 -- Decorators for Functions and Methods")
link.click()

time.sleep(3)

# driver.get("https://www.python.org/dev/peps/pep-0318/#examples")
link = driver.find_element_by_id("id80")
link.click()

time.sleep(8)

try:
	example_section = WebDriverWait(driver, 10). until(
		EC.presence_of_element_located((By.ID,"examples"))
	)

	examples = example_section.find_elements_by_class_name("first")
	print("Numarul de exemple este:",len(examples))
	# for exemplu_concret in examples:
	# 	print(exemplu_concret.text)
    # am si afisat cerinta pentru fiecare exemplu 

finally:
	driver.quit()




