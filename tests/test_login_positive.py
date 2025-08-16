"""
Positive automation tests for Login Form
"""
import pytest
from playwright.sync_api import expect
from data.data import UserData
from data.enum_data import MaskingPassword
from pages.gmail import Gmail
from pages.login import Login
from pages.main import Main


@pytest.mark.login_form
@pytest.mark.parametrize("input_data", [
    pytest.param(UserData.VALID_EMAIL.lower(),
                 id="Lower case"
                 ),
    pytest.param(UserData.VALID_EMAIL.upper(),
                 id="Upper case"
                 ),
], )
def test_email_valid_credentials(setup_teardown, input_data):
    """
    Validate case sensitivity of email field
    """
    login_page = setup_teardown

    login_page.sign_in(UserData.VALID_EMAIL, UserData.VALID_PASSWORD)

    # Validate if gmail page presented
    expect(login_page.gmail_page).to_be_visible(timeout=10000)


@pytest.mark.login_form
def test_masking_password(setup_teardown):
    """
    Validate masking password of password field
    """
    login_page = setup_teardown

    # Fill email into email input
    login_page.email_field.fill(UserData.VALID_EMAIL)
    login_page.next_button.click()

    # Fill password into password input
    login_page.password_field.fill(UserData.VALID_PASSWORD)

    # Validate unchecked checkbox by default before to be checked
    assert not login_page.show_password_checkbox.is_checked()

    # Grabbing attr value when checkbox in  default state
    attr_value_masked = login_page.password_field.get_attribute("type")

    # Validate masked password
    assert attr_value_masked == MaskingPassword.MASKED

    # Check the checkbox 'Show password'
    login_page.show_password_checkbox.check()

    # Validate checkbox after check
    assert login_page.show_password_checkbox.is_checked()

    # Grabbing attr value when checkbox is checked
    attr_value_unmasked = login_page.password_field.get_attribute("type")

    # Validate unmasked password when checkbox is checked
    assert attr_value_unmasked == MaskingPassword.UNMASKED


@pytest.mark.login_form
def test_restore_email(setup_teardown, get_context):
    """
    Validate the flow of restoring main email by using reserved email
    """
    main_email = setup_teardown

    # Click on 'Forgot Email' button to start the restoration process
    main_email.forgot_email_button.click()

    # Choose language before the restoration process
    main_email.choose_language()

    # Specify reserved email and name to restore the main email
    main_email.email_field.fill(UserData.RESERVED_EMAIL)
    main_email.next_button.click()
    main_email.name.fill(UserData.NAME)
    main_email.next_button.click()

    # Check 'Get verification code section'
    expect(main_email.get_ver_code_msg).to_be_visible()

    main_email.send_ver_code_button.click()

    # Check for new section that waits for verification code
    expect(main_email.enter_code).to_be_visible()

    # Create a new tab
    page_2 = get_context.new_page()
    google_account_page = Main(page_2)

    # Go to Gmail Login Form
    reserved_email: Login = google_account_page.go_to_login_form()

    # # Fill email into email input
    reserved_email.sign_in(UserData.RESERVED_EMAIL, UserData.VALID_PASSWORD)

    # Validate if gmail page presented
    expect(reserved_email.gmail_page).to_be_visible(timeout=10000)

    gmail_page = Gmail(reserved_email.page)
    # Check new email with a verification code
    expect(gmail_page.email).to_be_visible(timeout=5000)

    # Click on email and grab the verification code
    gmail_page.email.click()
    verification_code = gmail_page.code.text_content()

    # Delete the latest email with the verification code
    # TODO delete the last email could be realized in teardown using SMTP
    gmail_page.delete_last_email()
    expect(gmail_page.email).not_to_be_visible()
    gmail_page.page.close()

    # Enter the code
    main_email.enter_code_input.fill(verification_code)
    main_email.next_button.click()

    # Validate the restored email in the list of active accounts
    expect(main_email.restored_email).to_be_visible()
