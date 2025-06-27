# from pages dir import login and homepage classes
from pages.login_page import LoginPage
from pages.home_page import HomePage
# .env file use to store credential
# load_dotenv() used to get the credentials
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file
# store the username and password
username = os.getenv("ZEN_USERNAME")
password = os.getenv("ZEN_PASSWORD")


#  1. Test: Successful Login
def test_successful_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)
    home = HomePage(page)
    assert home.is_logged_in(), " Login failed or profile icon not visible"

    #  2. Test: Unsuccessful Login with Invalid Credentials

def test_unsuccessful_login(page):
     login = LoginPage(page)
     login.navigate()
     login.login("wronguser@example.com", "wrongpassword")
     # Check if still on login page or error appears
     assert page.url.endswith("login"), " Should not redirect on invalid login"

    #  3. Validate Username & Password Fields Present
def test_input_fields_validation(page):
    login = LoginPage(page)
    login.navigate()
    page.wait_for_selector("xpath=//input[@placeholder='Enter your mail']", timeout=5000)
    page.wait_for_selector("xpath=//input[@placeholder='Enter your password ']", timeout=5000)

    assert login.is_username_input_present(), "Username input not visible/enabled"
    assert login.is_password_input_present(), "Password input not visible/enabled"

    #  4. Validate Login Button is Clickable
def test_login_button_clickable(page):
    login = LoginPage(page)
    login.navigate()
    assert login.is_login_button_clickable(), " Login button not clickable"

    # 5. Validate Logout Functionality
def test_logout_functionality(page):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    home = HomePage(page)
    assert home.is_logged_in(), " Login failed before logout"
    home.logout()

    page.wait_for_url("**/login", timeout=5000)
    assert page.url.endswith("login"), " Logout did not redirect to login page"

# assertion are used here in each test case to verify what we need
# wait for used to time exception
# test cases use the each method in loginpage and homepage classes