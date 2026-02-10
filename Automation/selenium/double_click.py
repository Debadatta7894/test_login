from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/buttons")

double_clk = driver.find_element(By.ID, "doubleClickBtn")
actions = ActionChains(driver)
actions.double_click(double_clk).perform()

time.sleep(5)
driver.quit()
