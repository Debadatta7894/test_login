from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch Browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open your local HTML file
driver.get(r"C:\Users\HP\PycharmProjects\PythonProject\Automation\Exam\exam.html")

time.sleep(8)

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)




driver.find_element(By.ID, "name").send_keys("Debadatta")

time.sleep(1)

driver.find_element(By.ID, "male").click()

time.sleep(1)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
checkboxes[1].click()

time.sleep(2)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
checkboxes[2].click()

time.sleep(1)


Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

time.sleep(1)

driver.find_element(By.ID, "country_suggest").send_keys("Aus")
wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='Australia']"))).click()

time.sleep(1)

driver.find_element(By.ID,'dob').send_keys('26-02-2001')

time.sleep(1)

driver.find_element(By.XPATH, "//h4[text()='March 2026']/following::div[text()='3']").click()
driver.find_element(By.XPATH, "//h4[text()='April 2026']/following::div[text()='5']").click()

time.sleep(1)



driver.find_element(By.ID, "fileUpload").send_keys("C:/Users/HP/Downloads/AccountStatement_01-MAR-2025_to_01-SEP-2025.pdf")
driver.find_element(By.XPATH,'/html/body/section[8]/button')
time.sleep(3)


driver.find_element(By.XPATH, "//button[text()='Open New Tab']").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID, "tabInput").send_keys("Hello Tab")
driver.close()
time.sleep(4)
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
# open new window

driver.find_element(By.XPATH, "//button[text()='Alert']").click()
time.sleep(5)
wait.until(EC.alert_is_present()).accept()

time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
time.sleep(3)
wait.until(EC.alert_is_present()).dismiss()

driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
alert = wait.until(EC.alert_is_present())
print(alert.text)
alert.send_keys("Automation")
time.sleep(3)
alert.accept()


hover = driver.find_element(By.CLASS_NAME, "hover-box")
actions.move_to_element(hover).perform()


double_btn = driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
time.sleep(4)
actions.double_click(double_btn).perform()
time.sleep(3)
wait.until(EC.alert_is_present()).accept()


drag = driver.find_element(By.ID, "drag")
time.sleep(3)
drop = driver.find_element(By.ID, "drop")
time.sleep(3)
actions.drag_and_drop(drag, drop).perform()

time.sleep(3)


right_click = driver.find_element(By.ID, "rightClickBox")
actions.context_click(right_click).perform()

time.sleep(3)

driver.switch_to.frame("frame1")
driver.find_element(By.ID, "btn1").click()
driver.switch_to.default_content()

time.sleep(3)

driver.find_element(By.ID, "keyboardField1").send_keys("Hello")
driver.find_element(By.ID, "keyboardField1").send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys("World")

time.sleep(3)


driver.find_element(By.XPATH, "//button[text()='Submit']").click()



time.sleep(5)
driver.quit()