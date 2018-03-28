from selenium.webdriver.firefox.webdriver import WebDriver

# class with helpful for tests functions
class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        driver = self.driver

        self.driver.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        driver = self.driver

        self.open_home_page()

        # login
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_xpath("//input[@value='Login']").click()




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

    def logout(self):
        driver = self.driver

        # logout
        driver.find_element_by_link_text("Logout").click()

    def destroy(self):
        driver = self.driver

        self.driver.quit()