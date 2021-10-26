from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
time.sleep(3)

# link = driver.find_element_by_id("downloads")
# link.click()

element_to_hover_over = driver.find_element_by_link_text("Downloads")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

time.sleep(3)

link = driver.find_element_by_link_text("All releases")
link.click()

time.sleep(3)
try:
	elemente_tabel = WebDriverWait(driver, 10). until(
		EC.presence_of_element_located((By.CLASS_NAME,"main-content"))
	)

	versiuni = elemente_tabel.find_elements_by_class_name("release-version")
	
	print("ultima versiune din tabel este: ",versiuni[1].text)


finally:
	driver.quit()






