"""
Module to holding functionalities for Login Form page
"""
from data.data import InvalidOptionException, UserData
from data.enum_data import ErrorMessageOption
from pages.main import Page, Locator
from playwright.sync_api import expect
from typing import Any


class Login:
    """
    Class to holding functionalities for Login page
    """
    LOCATORS = {
        "login_page": "xpath=//div[contains(text(), 'Email or phone')]",
        "email_input": "xpath=//input[@type='email']",
        "next_button": {"role": "button",
                        "name": "Next"},
        "password_input": "xpath=//input[@name='Passwd']",
        "gmail_page": "xpath=//a[@aria-label='Inbox']",
        "email_error": "xpath=//{option}[contains(text(), "
                       "'{err_msg}')]",
        "show_password_checkbox": "xpath=//input[@type='checkbox']",
        "forgot_email_button": {"role": "button",
                                "name": "Forgot email?"},
        "name": "xpath=//input[@name='firstName']",

        "send_ver_code_button": {"role": "button",
                                 "name": "Send"},
        "get_ver_code_msg": "xpath=//span[contains(text(),"
                            " 'Get a verification code')]",
        "enter_code": "xpath=//span[contains(text(),"
                      " 'Enter the code')]",
        "enter_code_input": "xpath=//input[@type='tel']",
        "restored_email": f"xpath=//li/div[@data-identifier="
                          f"'{UserData.VALID_EMAIL}']",
        "language_combobox": "xpath=//div[@role='combobox']",
        "language": "//li[@data-value='{language}']"

    }

    def __init__(self, page: Page):
        self.page = page

    @property
    def login_page(self) -> Locator:
        """
        Locator for Sign in button

        :return: locator
        """
        return self.page.locator(self.LOCATORS["login_page"])

    @property
    def password_field(self) -> Locator:
        """
        Password field locator

        :return: locator
        """
        return self.page.locator(self.LOCATORS["password_input"])

    @property
    def email_field(self) -> Locator:
        """
        Email field locator

        :return: locator
        """
        return self.page.locator(self.LOCATORS["email_input"])

    @property
    def gmail_page(self) -> Locator:
        """
        Gmail Page

        :return: locator
        """
        return self.page.locator(self.LOCATORS["gmail_page"])

    @property
    def show_password_checkbox(self) -> Locator:
        """
        Show password checkbox in the password field section of Gmail
        Login Form

        :return: locator
        """
        return self.page.locator(self.LOCATORS["show_password_checkbox"])

    @property
    def next_button(self) -> Locator:
        """
        Next button at Password and Email sections

        :return: locator
        """
        return self.page.get_by_role(**self.LOCATORS["next_button"])

    @property
    def forgot_email_button(self) -> Locator:
        """
        Forgot email button to restore launch the process to resotre email
        :return:
        """
        return self.page.get_by_role(**self.LOCATORS["forgot_email_button"])

    @property
    def name(self) -> Locator:
        """
        Your name that requires for the restoration process

        :return: locator
        """
        return self.page.locator(self.LOCATORS["name"])

    @property
    def send_ver_code_button(self) -> Locator:
        """
        Button to send verification code to restore the email

        :return: locator
        """
        return self.page.get_by_role(**self.LOCATORS["send_ver_code_button"])

    @property
    def get_ver_code_msg(self) -> Locator:
        """
        Message 'Get a verification code'

        :return: locator
        """
        return self.page.locator(self.LOCATORS["get_ver_code_msg"])

    @property
    def enter_code(self) -> Locator:
        """
        Message 'Enter the code'

        :return: locator
        """
        return self.page.locator(self.LOCATORS["enter_code"])

    @property
    def enter_code_input(self) -> Locator:
        """
        Message 'Enter the code'

        :return: locator
        """
        return self.page.locator(self.LOCATORS["enter_code_input"])

    @property
    def restored_email(self) -> Locator:
        """
        Restored main email in the list of active emails accounts

        :return: locator
        """
        return self.page.locator(self.LOCATORS["restored_email"])

    @property
    def language_combobox(self) -> Locator:
        """
        Language combobox to restore the email

        :return: locator
        """
        return self.page.locator(self.LOCATORS["language_combobox"])

    def validate_error_message_by_option(self, option: ErrorMessageOption,
                                         err_msg: str) -> Any:
        """
        Method to click click next button depends on option
        if option is EMAIL then EMAIL argument should be provided
        if option is PASSWORD then PASSWORD

        :param option: EMAIL or PASSWORD
        :param err_msg: Basically the expected message to validate
        :return: None or AssertionError
        """
        options = {"EMAIL": 'div', "PASSWORD": "span"}
        op = options.get(option)
        if not op:
            raise InvalidOptionException(f"Your option: {option} is invalid. "
                                         f"Check available options to choose "
                                         f"the right one:"
                                         f" {tuple(options.keys())}")
        path_to_elem = self.LOCATORS['email_error'].format(option=op,
                                                           err_msg=err_msg)
        locator = self.page.locator(path_to_elem)
        expect(locator).to_have_text(err_msg)

    def choose_language(self, language="en") -> None:
        """
        Choose language from combobox when launch the flow of restoring email

        :param language: get language option according to @data-value.
        'en' option by default
        :return: None
        """
        self.language_combobox.click()
        xpath = self.LOCATORS["language"].format(language=language)
        self.page.locator(xpath).click()
