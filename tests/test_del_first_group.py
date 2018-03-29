# -*- coding: utf-8 -*-
# from selenium.webdriver.chrome import webdriver

from model.group import Group

# test
def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


