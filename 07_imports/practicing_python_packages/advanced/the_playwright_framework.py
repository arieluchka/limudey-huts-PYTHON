# need to install the playwright package

"""
pip install playwright
playwright install
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()