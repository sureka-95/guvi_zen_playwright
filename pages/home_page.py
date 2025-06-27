# page is main class from Playwright to interact with a web page
# PlaywrightTimeoutError handles timeout exceptions.
# LoginPageLocators used to separate file where XPaths/CSS selectors for login elements are defined.
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

# create class for homepage
class HomePage:
    def __init__(self, page: Page):# initiallization
        self.page = page
        # assign xpath by using pagelocators
        self.profile_icon = page.locator("xpath=//p[@class='avatar-profile-name d-flex fs-normal m-0']")
        self.logout_link = page.locator("xpath=//div[normalize-space()='Log out']")
# define logout method use try and exeption block
    def logout(self):
        try:
            # wait_for used to wait certain condition reach
            #  milli seconds is used
            self.profile_icon.wait_for(state="visible", timeout=5000)
            self.profile_icon.click()
            self.logout_link.wait_for(state="visible", timeout=5000)
            self.logout_link.click()
            # except  print if any error occur
        except PlaywrightTimeoutError as e:
            print(f"Logout failed: {e}")
            raise
# define is_logged_in method with exceptions
    def is_logged_in(self):
        try:
            self.profile_icon.wait_for(state="visible", timeout=5000)
            return self.profile_icon.is_visible()
        except:
            return False
# define logout visible method used to verify is visbile or not
    def is_logout_visible(self):
       try:
           return self.logout_link.is_visible()
       except PlaywrightTimeoutError:
           return False
