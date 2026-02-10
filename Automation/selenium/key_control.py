from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
time.sleep(5)


name = driver.find_element(By.ID,"userName")
name.send_keys("Debadatta jena")


name.send_keys(Keys.CONTROL+"a")
name.send_keys(Keys.CONTROL+"c")


email = driver.find_element(By.ID,"userEmail")
email.send_keys(Keys.CONTROL+'v')
time.sleep(5)
driver.quit()