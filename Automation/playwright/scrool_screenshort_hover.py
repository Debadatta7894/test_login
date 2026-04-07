from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()

 page.goto(r"https://rahulshettyacademy.com/AutomationPractice/")

#Mouse hover
 # hover_btn = page.locator("#mousehover")
 # hover_btn.scroll_into_view_if_needed()
 # hover_btn.hover()
 # time.sleep(3)
 # print(page.locator("a[href='#top']").text_content())
 # page.click("a[href='#top']")


#screemshot
#way-1 :- full page screenshot
# page.screenshot(path=r'C:\Users\HP\PycharmProjects\PythonProject\Automation\playwright\p_screenshort\fullpage.png',full_page=True)

#wway -2 Element screenshot
 # page.locator("#courses-iframe").scroll_into_view_if_needed()
 # frame = page.locator("#courses-iframe")
 # frame.screenshot(
 # path=r'C:\Users\HP\PycharmProjects\PythonProject\Automation\playwright\p_screenshort\frame_fullpage.png')


 # page.locator("(//table[@id='product'])[1]").scroll_into_view_if_needed()
 # table = page.locator("(//table[@id='product'])[1]")
 # table.screenshot(path = "table.png")
 # time.sleep(3)


#scroll

#scroll dowm
#way1
 # page.mouse.wheel(0,1000)
 # time.sleep(2)

#way2- js



 page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
 time.sleep(2)
 page.mouse.wheel(0,-1000)




 # page.evaluate("_window_.scrollTo(0,-1000)")
 # time.sleep(2)

 browser.close()
