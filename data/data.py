"""
This module collects env variables
"""

MAIN_PAGE_URL = "https://workspace.google.com/intl/en-US/gmail"


class UserData:
    """
    Credentials required for testing gmail login form
    """
    VALID_EMAIL = "testtaskdelphi@gmail.com"
    NAME = "testtaskdelphi"
    RESERVED_EMAIL = "testtaskdelphi1@gmail.com"  # email to restore the main
    VALID_PASSWORD = "test123test"


class InvalidData:
    """
    Class the stores data for the negative test cases
    """
    INVALID_EMAIL_FORMAT = "testtaskdelphigmail@.com"
    INVALID_PASSWORD = "1111111111111111"
    EMPTY_FIELD = ""


class ErrorMessages:
    """
    Class that stores error messages
    """
    NO_GOOGLE_ACCOUNT = "Enter a valid email or phone number"
    ENTER_EMAIL_OR_NUMBER = "Enter an email or phone number"
    WRONG_PASSWORD = "Wrong password. Try again or click Forgot password to " \
                     "reset it."
    ENTER_PASSWORD = "Enter a password"


class InvalidOptionException(Exception):
    """
    This exception raises when invalid option is provided
    """
