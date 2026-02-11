from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class SignupPage(BasePage):
    LOGIN_LINK = (By.XPATH,"//p[normalize-space()='Login']")
    SIGNUP_LINK = (By.XPATH,"//a[normalize-space()='Sign Up']")
    CHECKBOX_BUTTON = (By.XPATH,"//button[@id='remember']")
    CONTINUE_BUTTON = (By.XPATH,"//button[normalize-space()='Continue']")

    # Set up your account locaters
    FIRST_NAME = (By.NAME,"firstName")
    LAST_NAME = (By.NAME,"lastName")
    EMAIL = (By.XPATH,"//input[@placeholder='Enter Your Email Address']")
    PHONE_NUMBER = (By.NAME,"phoneNumber")
    PASSWORD = (By.XPATH,"//input[@name='password']")
    CONFIRM_PASSWORD = (By.XPATH,"//input[@name='confirmPassword']")
    NEXT_BUTTON1 = (By.XPATH,"//button[normalize-space()='Next']")

    # OTP locators
    OTP_FIELD = (By.XPATH, "//input[@class='disabled:cursor-not-allowed']")
    VERIFY_CODE_BUTTON = (By.XPATH, "//button[normalize-space()='Verify Code']")
    RESEND_BUTTON = (By.XPATH, "//span[@class='text-primary cursor-pointer']")

    # AgencyDetails locaters
    AGENCY_NAME = (By.NAME,"agency_name")
    AGENCY_ROLE = (By.NAME,"role_in_agency")
    AGENCY_EMAIL = (By.NAME,"agency_email")
    AGENCY_WEBSITE = (By.NAME,"agency_website")
    AGENCY_ADDRESS = (By.NAME,"agency_address")
    REGION_OF_OPERATION = (By.XPATH,"//button[@role='combobox']")
    REGION_SELECTION = (By.XPATH,"//span[normalize-space()='Australia']")
    NEXT_BUTTON2 = (By.XPATH,"//button[normalize-space()='Next']")

    # ProfessionalExperience locaters
    EXPERIENCE_YEARS = (By.XPATH,"//button[normalize-space()='Select Your Experience Level']")
    CLICK_EXPERIENCE =(By.XPATH,"//span[normalize-space()='1 year']")
    STUDENTS_RECRUITED =(By.NAME,"number_of_students_recruited_annually")
    FOCUS_AREA = (By.NAME,"focus_area")
    SUCCESS_METRICS = (By.NAME,"success_metrics")
    SERVICES_PROVIDED1 = (By.XPATH,"//label[normalize-space()='Career Counseling']")
    SERVICES_PROVIDED2 = (By.XPATH,"//label[normalize-space()='Admission Applications']")
    SERVICES_PROVIDED3 = (By.XPATH,"//label[normalize-space()='Visa Processing']")
    SERVICES_PROVIDED4 = (By.XPATH,"//label[normalize-space()='Test Prepration']")
    NEXT_BUTTON3 = (By.XPATH,"//button[normalize-space()='Next']")

    # Verification and Preferences locaters
    BUSINESS_REGISTRATION_NUMBER = (By.NAME,"business_registration_number")
    PREFERRED_COUNTRIES = (By.XPATH,"//span[normalize-space()='Select Your Preferred Countries']")
    CLICK_PREFERREDCOUNTRIES = (By.XPATH,"//span[normalize-space()='Australia']")
    PREFERRED_INSTITUTION = (By.XPATH,"//label[normalize-space()='Universities']")
    FILEUPLOAD = (By.XPATH,"//div[@class='h-fit flex flex-col lg:justify-center gap-6']//div//div[1]//div[1]//div[1]//div[1]//span[1]")
    SUBMIT_BUTTON = (By.XPATH,"//button[normalize-space()='Submit']")
    PROFILE_NAME = (By.XPATH,"//h3[@class='text-[20px] font-satoshi-bold leading-snug']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)

    def click_signup_link(self):
        self.click_element(self.SIGNUP_LINK)

    def click_checkbox_button(self):
        self.click_element(self.CHECKBOX_BUTTON)

    def click_continue_button(self):
        self.click_element(self.CONTINUE_BUTTON)

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME, last_name)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_phone_number(self, phone_number):
        self.enter_text(self.PHONE_NUMBER, phone_number)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def enter_confirm_password(self, confirm_password):
        self.enter_text(self.CONFIRM_PASSWORD,confirm_password)

    def click_next_button1(self):
        self.click_element(self.NEXT_BUTTON1)

    def enter_otp(self, otp):
        self.enter_text(self.OTP_FIELD,otp)

    def click_verify_code_button(self):
        self.click_element(self.VERIFY_CODE_BUTTON)

    def enter_agency_name(self, agency_name):
        self.enter_text(self.AGENCY_NAME, agency_name)

    def enter_agency_role(self, agency_role):
        self.enter_text(self.AGENCY_ROLE,agency_role)

    def enter_agency_email(self, agency_email):
        self.enter_text(self.AGENCY_EMAIL, agency_email)

    def enter_agency_website(self, agency_website):
        self.enter_text(self.AGENCY_WEBSITE, agency_website)

    def enter_agency_address(self, agency_address):
        self.enter_text(self.AGENCY_ADDRESS, agency_address)

    def select_region_of_operation(self):
        self.click_element(self.REGION_OF_OPERATION)
        self.click_element(self.REGION_SELECTION)

    def click_next_button2(self):
        self.click_element(self.NEXT_BUTTON2)

    def select_experience_year(self):
        self.click_element(self.EXPERIENCE_YEARS)
        self.click_element(self.CLICK_EXPERIENCE)

    def enter_students_recruited(self, students_recruited):
        self.enter_text(self.STUDENTS_RECRUITED, students_recruited)

    def enter_focus_area(self, focus_area):
        self.enter_text(self.FOCUS_AREA, focus_area)

    def enter_success_metrics(self, success_metrics):
        self.enter_text(self.SUCCESS_METRICS, success_metrics)

    def select_services(self):
        self.click_element(self.SERVICES_PROVIDED1)
        self.click_element(self.SERVICES_PROVIDED2)
        self.click_element(self.SERVICES_PROVIDED3)
        self.click_element(self.SERVICES_PROVIDED4)

    def click_next_button3(self):
        self.click_element(self.NEXT_BUTTON3)

    def enter_business_registration_number(self, business_registration_number):
        self.enter_text(self.BUSINESS_REGISTRATION_NUMBER, business_registration_number)

    def select_preferred_countries(self):
        self.click_element(self.PREFERRED_COUNTRIES)
        self.click_element(self.CLICK_PREFERREDCOUNTRIES)

    def select_preferred_institution(self):
        self.click_element(self.PREFERRED_INSTITUTION)

    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON)

