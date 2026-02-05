from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script('window.scrollBy(0,900);')
time.sleep(3)

driver.switch_to.frame('courses-iframe')
heading_text=driver.find_element(By.XPATH,'//h2').text
print(heading_text)

driver.find_element(By.XPATH,"//a[text()='All Access plan']").click()
time.sleep(3)

driver.switch_to.default_content()
driver.find_element(By.ID,"name").send_keys('Default frame')
time.sleep(2)
driver.close()