# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_homePage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groupsPage(wd)
        self.create_group(wd, Group(name="test", header="test", footer="test"))
        self.return_to_groupsPage(wd)
        self.loguot(wd)

    def test_add_emptygroup(self):
        wd = self.wd
        self.open_homePage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groupsPage(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_groupsPage(wd)
        self.loguot(wd)

    def loguot(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groupsPage(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init new group
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groupsPage(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_homePage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
