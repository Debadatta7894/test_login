from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os

download_dir = r"C:\file_dow"

chrome_options = Options()

pref = {
"download.default_directory":download_dir,
"download.prompt_for_download":False,
"directory_upgrade": True
}
chrome_options.add_experimental_option("prefs",pref)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/download')
time.sleep(5)

driver.find_element(By.LINK_TEXT,'Image.PNG').click()
time.sleep(4)

file_path=os.path.join(download_dir)
print('downloaded:',os.path.exists(file_path))

driver.quit()