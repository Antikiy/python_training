
class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
            driver = self.app.driver

            # open groups page
            driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
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

    def delete_first_group(self):
        driver = self.app.driver
        # open groups page
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        # returns to groups page
        driver.find_element_by_link_text("groups").click()