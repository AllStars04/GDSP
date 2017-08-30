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

@then('click on link "{linkname}"')
def clickonlink(self,linkname):
    driver.clickOnLink(linkname)

@then('click on button "{btnname}"')
def clickonButton(self, btnname):
    driver.clickOnButton(btnname)

@then('enter text area for "{FieldName}" with value "{FieldValue}"')
def enterTextArea(self, FieldName,FieldValue):
    driver.enterTextArea(FieldName,FieldValue)

@then('logout and close the browser')
def logout(self):
    driver.logout()

