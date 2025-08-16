"""
Negative automation tests for Login Form
"""
import pytest

from data.data import InvalidData, ErrorMessages as ErrMsg, UserData
from data.enum_data import ErrorMessageOption as Option


@pytest.mark.login_form
@pytest.mark.parametrize("input_data, err_msg", [
    pytest.param(
        InvalidData.INVALID_EMAIL_FORMAT, ErrMsg.NO_GOOGLE_ACCOUNT,
        id="Invalid email field"
    ),
    pytest.param(
        InvalidData.EMPTY_FIELD, ErrMsg.ENTER_EMAIL_OR_NUMBER,
        id="Empty email field"
    ),
], )
def test_invalid_email(setup_teardown, input_data, err_msg):
    """
    Validate negative cases with empty and invalid inputs for Email field
    """
    login_page = setup_teardown

    # Fill invalid email value into email input
    login_page.email_field.fill(input_data)
    login_page.next_button.click()

    # Validate error message
    login_page.validate_error_message_by_option(Option.EMAIL, err_msg)


@pytest.mark.login_form
@pytest.mark.parametrize("input_data, err_msg", [
    pytest.param(
        InvalidData.INVALID_PASSWORD, ErrMsg.WRONG_PASSWORD,
        id="Invalid password field"
    ),
    pytest.param(
        InvalidData.EMPTY_FIELD, ErrMsg.ENTER_PASSWORD,
        id="Empty password field",
    ),
], )
def test_invalid_password(setup_teardown, input_data, err_msg):
    """
    Validate negative cases with empty and invalid inputs for Password field
    """
    login_page = setup_teardown

    # Fill valid email value into email input
    login_page.email_field.fill(UserData.VALID_EMAIL)
    login_page.next_button.click()

    # Fill invalid password value into email input
    login_page.password_field.fill(input_data)
    # login_page.password_field.clear()
    login_page.next_button.click()

    # Validate error message
    login_page.validate_error_message_by_option(Option.PASSWORD, err_msg)
