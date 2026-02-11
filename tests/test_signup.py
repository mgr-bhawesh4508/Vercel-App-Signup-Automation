import pytest
from pages.signup_page import SignupPage
from utils.test_runner import create_driver
from utils.otp_reader import create_temp_email, get_token, get_otp
from utils.upload_File import upload_file
from data.test_data import VALID_DATA
from utils.assertions import assert_true
import time
import allure

class TestSignup:
    def setup_method(self):
        self.driver = create_driver()
        self.signup_page = SignupPage(self.driver)

        self.driver.get("https://authorized-partner.vercel.app/")

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing User Signup")
    @pytest.mark.parametrize("valid_data", VALID_DATA)
    def test_user_signup(self, valid_data):
        with allure.step("Click Login link"):
            self.signup_page.click_login_link()
            time.sleep(2)
            assert_true("login" in self.driver.current_url, "User is not on the login page","login_link",self.signup_page)

        with allure.step("Click Signup link"):
            self.signup_page.click_signup_link()
            time.sleep(2)
            assert_true("register" in self.driver.current_url, "User is not on the signup page","Signup_link",self.signup_page)

        with allure.step("Check privacy policy checkbox and click on continue"):
            self.signup_page.click_checkbox_button()
            self.signup_page.click_continue_button()

        with allure.step("Filling out signup details and otp verification"):
            # Create temp email
            email, password = create_temp_email()
            token = get_token(email, password)

            self.signup_page.enter_first_name(valid_data["first_name"])
            self.signup_page.enter_last_name(valid_data["last_name"])
            self.signup_page.enter_email(email)  # use temp email here
            self.signup_page.enter_phone_number(valid_data["phone_number"])
            time.sleep(3)
            self.signup_page.enter_password(valid_data["password"])
            self.signup_page.enter_confirm_password(valid_data["confirm_password"])
            self.signup_page.click_next_button1()

            # Get OTP dynamically
            otp = get_otp(token)

            self.signup_page.enter_otp(otp)
            self.signup_page.click_verify_code_button()

        with allure.step("Filling out Agency Details"):
            self.signup_page.enter_agency_name(valid_data["agency_name"])
            self.signup_page.enter_agency_role(valid_data["agency_role"])
            self.signup_page.enter_agency_email(valid_data["agency_email"])
            self.signup_page.enter_agency_website(valid_data["agency_website"])
            self.signup_page.enter_agency_address(valid_data["agency_address"])
            self.signup_page.select_region_of_operation()
            self.signup_page.click_next_button2()

        with allure.step("Filling out Professional Experience"):
            self.signup_page.select_experience_year()
            self.signup_page.enter_students_recruited(valid_data["students_recruited"])
            self.signup_page.enter_focus_area(valid_data["focus_area"])
            self.signup_page.enter_success_metrics(valid_data["success_metrics"])
            self.signup_page.select_services()
            self.signup_page.click_next_button3()

        with allure.step("Filling out Verification and Preferences"):
            self.signup_page.enter_business_registration_number(valid_data["business_registration_number"])
            self.signup_page.select_preferred_countries()
            self.signup_page.select_preferred_institution()
            time.sleep(5)
            upload_file(self.driver)
            self.signup_page.click_submit_button()

        with allure.step("Verify successful signup and profile name"):
            # Wait until profile name is visible
            self.signup_page.is_element_visible(self.signup_page.PROFILE_NAME)

            # Get actual profile name
            actual_profile_name = self.signup_page.get_element_text(self.signup_page.PROFILE_NAME)

            # Expected profile name
            expected_profile_name = f"{valid_data['first_name']} {valid_data['last_name']}"

            # Single strong assertion
            assert_true(actual_profile_name == expected_profile_name,
                f"Signup failed. Expected profile name: {expected_profile_name}, "
                f"but found: {actual_profile_name}",
                "Signup_Profile_Validation", self.signup_page
            )

