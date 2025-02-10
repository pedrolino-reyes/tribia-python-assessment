import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from the .env file
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:3000")

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture
def browser_context(playwright_instance, base_url):
    browser = playwright_instance.chromium.launch()
    context = browser.new_context(base_url=base_url)
    yield context
    browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()
