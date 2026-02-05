from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# Store parent window
parent_window = driver.current_window_handle
print("Parent Window:", parent_window)



driver.find_element(By.ID,"openwindow").click()
time.sleep(7)
# Click link that opens new window/tab
# driver.find_element(By.LINK_TEXT, "Home").click()
# time.sleep(2)
#
# driver.find_element(By.LINK_TEXT, "Sign Up").click()
# time.sleep(5)









all_windows = driver.window_handles
print(all_windows)


for wnd in all_windows:
    if wnd != parent_window:
        driver.switch_to.window(wnd)
        break

print("Child window title:", driver.title)

driver.find_element(By.LINK_TEXT, "Courses").click()
time.sleep(5)



driver.close()

# Switch back to parent window
driver.switch_to.window(parent_window)
print("Back to Parent:", driver.title)





# driver.find_element(By.XPATH,"//input[@name='name']").click()
# name_input=wait.until(EC.alert_is_present())
# name_input.send_keys('Debadatta Jena')
# time.sleep(2)






time.sleep(5)
driver.quit()







