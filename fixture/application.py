from selenium.webdriver.firefox.webdriver import WebDriver
from session import SessionHelper
from group import GroupHelper

# class with helpful for tests functions
class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver

        self.driver.get("http://localhost/addressbook/index.php")

    def destroy(self):
        driver = self.driver
        self.driver.quit()