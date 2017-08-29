from behave import *
import Class.Automation
import Module.Utility

driver = Class.Automation.Automation()
@given('start test case')
def starttestcase(self):
    print("Test case start")

@given('open browser')
def openbrowser(self):
    driver.openURL()

@when('login into portal')
def login(self):
    driver.login()

@when('click on menu "{menuname}"')
def clickonmenu(self,menuname):
    driver.clickOnMenu(menuname)

@then('click on submenu "{submenuname}"')
def clickonmenu(self,submenuname):
    driver.clickOnMenu(submenuname)

@when('text "{textname}" is visible')
def verifytext(self,textname):
    driver.verifyTextOnScreen(textname)
