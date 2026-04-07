from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()

 page.goto(r"https://rahulshettyacademy.com/AutomationPractice/")