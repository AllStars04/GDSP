from behave import *
import Class.Automation
import Module.Utility
import Module.logger

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

@then('click on input "{inputname}"')
def clickonmenu(self,inputname):
    driver.clickOnInput(inputname)

@then('select from list "{optionname}"')
def clickonmenu(self,optionname):
    driver.selectFromList(optionname)

@then('click on list "{optionname}"')
def clickonmenu(self,optionname):
    driver.clickOnList(optionname)

@when('text "{textname}" is visible')
def verifytext(self,textname):
    driver.verifyTextOnScreen(textname)

@then('click on link "{linkname}"')
def clickonlink(self,linkname):
    driver.clickOnLink(linkname)

@then('click on button "{btnname}"')
def clickonButton(self, btnname):
    driver.clickOnButton(btnname)

@then('enter text for "{FieldName}" with value "{FieldValue}"')
def enterTextArea(self, FieldName,FieldValue):
    driver.enterText(FieldName,FieldValue)

@then('enter text area for "{FieldName}" with value "{FieldValue}"')
def enterTextArea(self, FieldName,FieldValue):
    driver.enterTextArea(FieldName,FieldValue)

@then('select option "{optionname}" of dropdown "{dropdownname}"')
def selectDropDownOption(self,dropdownname,optionname):
	driver.selectDropDownOption(dropdownname,optionname)
	
@then('validate table headers "{tableHeaders}" for table "{tableName}"')
def verifyTableColumnHeaders(self, tableName,tableHeaders):
    driver.verifyTableColumnHeaders(tableName,tableHeaders)

@then('logout and close the browser')
def logout(self):
    driver.logout()

@then('report info "{msg}"')
def info(self,msg):
    Module.logger.INFO(msg)

@then('get value from label "{lblName}" and store it in "{storeValue}"')
def getValueFromLabelAndStore(self, lblName,storeValue):
    lblText = driver.getValueFromLabel(lblName)
    driver.addValueToDic(storeValue,lblText)

@then('check if values "{value1}" and "{value2}" are "{operation}"')
def compareTwoValues(self,value1,value2,operation):
    driver.compareTwoValues(value1,value2,operation)

@then('select drop down "{dropDownName}" with option "{optionValue}"')
def selectDropDown(self,dropDownName,optionValue):
    driver.selectDropDownOption(dropDownName,optionValue)

@then('get all cols')
def getallcols(self):
    driver.getValueFromTable()