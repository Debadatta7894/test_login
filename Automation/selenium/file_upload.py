from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(5)

full_path = r"C:\Users\HP\Downloads\AccountStatement_UPDATED.docx"

upload_input = driver.find_element(By.ID,"file-upload")
upload_input.send_keys(full_path)

driver.find_element(By.ID,'file-submit').click()
time.sleep(5)
driver.quit()