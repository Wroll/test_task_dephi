# pylint: disable=missing-module-docstring
import pytest
from playwright.sync_api import Playwright
from pages.main import Main


@pytest.fixture()
def get_context(browser, playwright: Playwright):
    """
    Fixture to get a context in case for the cases when new tab required
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    yield browser.new_context(locale='en-US')
    browser.close()


@pytest.fixture
def setup_teardown(get_context):
    """
    Setup teardown fixture

    Executes steps to reach gmail login form
    """

    page = get_context.new_page()

    google_account_page = Main(page)

    login_page = google_account_page.go_to_login_form()
    yield login_page
