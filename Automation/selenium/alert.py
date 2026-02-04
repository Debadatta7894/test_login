from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait=WebDriverWait(driver,10)


# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# alert=wait.until(EC.alert_is_present())
# print(alert.text)
# alert.accept()

# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# alert=wait.until(EC.alert_is_present())
# print(alert.text)
# # alert.accept()
# alert.dismiss()

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
alert=wait.until(EC.alert_is_present())
print(alert.text)
alert.send_keys('Python automation')
alert.accept()


time.sleep(10)