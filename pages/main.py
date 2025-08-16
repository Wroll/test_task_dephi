"""
Module that holds functionality for Google account main page
"""
from playwright.sync_api import Page, expect
from playwright.sync_api._generated import Locator
from pages.login import Login
from data.data import MAIN_PAGE_URL


class Main:
    """
    Class to holding functionalities or Google account main page
    """

    LOCATORS = {
        "sign_in_button": {"role": "link",
                           "name": "Open the Sign into Gmail page"},
        "main_page": "xpath=//div[@class='header__logos']"}

    def __init__(self, page: Page):
        self.page = page

    @property
    def sign_in(self) -> Locator:
        """
        Locator for Sign in button

        :return: locator
        """
        return self.page.get_by_role(**self.LOCATORS["sign_in_button"])

    @property
    def main_page(self) -> Locator:
        """
        Locator for title

        :return: locator
        """
        return self.page.locator(self.LOCATORS["main_page"])

    def go_to_login_form(self):
        self.page.goto(MAIN_PAGE_URL)
        expect(self.main_page).to_be_visible()

        self.sign_in.click()

        login_page = Login(self.page)
        expect(login_page.login_page).to_be_visible()

        return login_page
