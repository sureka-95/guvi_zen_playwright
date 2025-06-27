# page is main class from Playwright to interact with a web page
# PlaywrightTimeoutError handles timeout exceptions.
# LoginPageLocators used to separate file where XPaths/CSS selectors for login elements are defined.
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from locators.login_page_locators import LoginPageLocators

#create a loginpage class
class LoginPage:
    def __init__(self, page: Page): # initialization
        self.page = page
        # locator used to find xpath
        self.username_input = page.locator(f"xpath={LoginPageLocators.USERNAME_INPUT}")
        self.password_input = page.locator(f"xpath={LoginPageLocators.PASSWORD_INPUT}")
        self.login_button = page.locator(f"xpath={LoginPageLocators.LOGIN_BUTTON}")

    def navigate(self):# navigate method
        self.page.goto("https://v2.zenclass.in/login")# navigate to zen portal

# define login method and pass arguments
    def login(self, username, password):
        # create try exception block ensures the elements are loaded and interactable before acting on them
        try:
            # wait for used to waits until element is visible or attached to DOM
            # fill the input field and  then click
            self.username_input.wait_for(state="visible", timeout=5000)
            self.username_input.fill(username)

            self.password_input.wait_for(state="visible", timeout=5000)
            self.password_input.fill(password)

            self.login_button.wait_for(state="attached", timeout=5000)
            self.login_button.click()
 # print the below line if there is any error raised
        except PlaywrightTimeoutError as e:
            print("Login form did not load properly or element not found.")
            raise e
# define method for username input is present to check visiblity
    def is_username_input_present(self):
        return self.username_input.is_visible() and self.username_input.is_enabled()
# define method for click login button
    def is_login_button_clickable(self):
        return self.login_button.is_enabled()
#define method to check password field is visible
    def is_password_input_present(self):
        return self.password_input.is_visible() and self.password_input.is_enabled()



