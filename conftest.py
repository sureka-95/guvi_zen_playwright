#import pytest
#import playwright in synchronous mode
import pytest
from playwright.sync_api import sync_playwright

# """ fixture used to create newpage for every test
#  and fresh browser context is created for each test """

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
