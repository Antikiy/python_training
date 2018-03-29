# -*- coding: utf-8 -*-
# from selenium.webdriver.chrome import webdriver

from model.group import Group

# test
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test_group", header="test", footer="test1"))
    app.session.logout()


# test
def test_add_group2(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test_group1", header="test1", footer="test2"))
    app.session.logout()
