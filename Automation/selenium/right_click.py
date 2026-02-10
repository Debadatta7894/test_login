from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(4)

button = driver.find_element(By.CSS_SELECTOR,".context-menu-one")

action = ActionChains(driver)
action.context_click(button).perform(button)
time.sleep(5)