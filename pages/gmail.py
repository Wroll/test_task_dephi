"""
Module that represents functionality for Gmail page
"""
from playwright.sync_api import Page
from playwright.sync_api._generated import Locator


class Gmail:
    """
    Class that represents functionality for Gmail page
    """
    LOCATORS = {
        "email": "xpath=//div[@class='UI']//tr",
        "code": "xpath=(//strong)[1]",
        "more_actions": "xpath=//div[@aria-label='More message options']",
        "delete_msg_action": "xpath=//div[@id='tm']",
    }

    def __init__(self, page: Page):
        self.page = page

    @property
    def email(self) -> Locator:
        """
        Email with a code

        :return: locator
        """
        return self.page.locator(self.LOCATORS["email"])

    @property
    def code(self) -> Locator:
        """
        Verification code

        :return: locator
        """
        return self.page.locator(self.LOCATORS["code"])

    @property
    def more_actions(self) -> Locator:
        """
        More actions

        :return: locator
        """
        return self.page.locator(self.LOCATORS["more_actions"])

    @property
    def delete_msg_action(self) -> Locator:
        """
        Delete message action

        :return: locator
        """
        return self.page.locator(self.LOCATORS["delete_msg_action"])

    def delete_last_email(self) -> None:
        """
        Delete the last messaged from reserved email

        :return: None
        """
        self.more_actions.click()
        self.delete_msg_action.click()
