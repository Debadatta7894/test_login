from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)



driver.execute_script("window.scrollBy(0,1000);")
time.sleep(5)


mouse_hover = driver.find_element(By.ID,"mousehover")
action = ActionChains(driver)



action.move_to_element(mouse_hover).perform()
time.sleep(4)


# driver.find_element(By.LINK_TEXT,"Top").click()
# time.sleep(5)

driver.find_element(By.LINK_TEXT,"Reload").click()
time.sleep(5)



time.sleep(5)
driver.quit()
