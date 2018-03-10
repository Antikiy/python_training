# -*- coding: utf-8 -*-
#from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.WebDriver()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost/addressbook/index.php")

    def login(self, driver, username, password):
        # login
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self, driver):
        # open groups page
        driver.find_element_by_link_text("groups").click()

    def create_new_group(self, driver, group):
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

    def logout(self, driver):
        # logout
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


    #test
    def test_add_group(self):
        driver = self.driver

        self.login(driver, username = "admin", password = "secret")
        self.open_groups_page(driver)
        self.create_new_group(driver, Group(name = "test_group", header ="test", footer = "test1"))
        self.logout(driver)

    #test
    def test_add_group2(self):
        driver = self.driver

        self.login(driver, username = "admin", password = "secret")
        self.open_groups_page(driver)
        self.create_new_group(driver, Group(name = "test_group1", header ="test1", footer = "test2"))
        self.logout(driver)

if __name__ == "__main__":
    unittest.main()
