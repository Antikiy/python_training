from selenium.webdriver.firefox.webdriver import WebDriver
from session import SessionHelper

# class with helpful for tests functions
class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver

        self.driver.get("http://localhost/addressbook/index.php")

    def open_groups_page(self):
        driver = self.driver

        # open groups page
        driver.find_element_by_link_text("groups").click()

    def create_new_group(self, group):
        driver = self.driver

        # open groups page
        self.open_groups_page()

        # create new group
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver

        # returns to groups page
        driver.find_element_by_link_text("groups").click()



    def destroy(self):
        driver = self.driver

        self.driver.quit()