import pytest
import sys
import os
from playwright.sync_api import sync_playwright

# Add the parent directory to the Python path so we can import the config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright_config import PlaywrightConfig

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": PlaywrightConfig.viewport,
        "ignore_https_errors": True,
    }

@pytest.fixture
def page(browser):
    context = browser.new_context(**browser_context_args())
    page = context.new_page()
    yield page
    context.close()
