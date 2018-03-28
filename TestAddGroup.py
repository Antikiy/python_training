# -*- coding: utf-8 -*-
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
import unittest
import pytest
from group import Group
from application import Application

# method where fixture is creating and destroying
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# test
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="test_group", header="test", footer="test1"))
    app.logout()


# test
def test_add_group2(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="test_group1", header="test1", footer="test2"))
    app.logout()
