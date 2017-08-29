# import Module.Utility
# import Module.ClickOnButton
# import Module.clickOnMenuAndSubmenu
# import Module.enterText
# import Class.SeleniumDriver
# import Module.verifyTextOnScreen
# import Module.selectDropDownOption
#
#
# Class.SeleniumDriver.getWebDriver()
# Class.SeleniumDriver.openUrl()
# Class.SeleniumDriver.login()
# Class.SeleniumDriver.gotodefaultframe()
# Module.clickOnMenuAndSubmenu.clickOnMenuAndSubmenu("Take a Call","Customer")
# Class.SeleniumDriver.gotocorrectframe()
# Module.enterText.enterText("MSISDN","40720011515")
# Module.ClickOnButton.clickOnButton("Search")
# Module.verifyTextOnScreen.verifyTextOnScreen("Verify Customer")
# Module.selectDropDownOption.selectDropDownOption("ID Number(10)","National ID")
# Module.selectDropDownOption.selectDropDownOption("Currency","USD")
# Module.ClickOnButton.clickOnButton("Pass")
# Module.ClickOnButton.clickOnButton("Verify")
# Module.ClickOnButton.clickOnButton("Customer Info")
#
#
# print(Module.Utility.ReadDataFromJsonFile("tool","browserType"))
# print(Module.Utility.ReadDataFromJsonFile("sut","url"))
#
#import pytest
import Class.Automation
import time
import Module.Utility

# idtype,idvalue = Module.Utility.CheckIfDefinedElementExistInRepo("text1","MSISDN")
#
# print(idtype)
# print(idvalue)
def test():
    obj = Class.Automation.Automation()
    obj.openURL()
    obj.enterText("UserName","Lavanya")


test()

def test1():
    obj = Class.Automation.Automation()
    obj.openURL()
    obj.login()
    #obj.fnClickOnCertificateIfExist()
    obj.clickOnMenu("Search")
    obj.clickOnSubmeu("Service Provider")
    obj.clickOnLink("Initiate Transaction")
    obj.selectDropDownOption("Transaction Type","Journal Entry Transaction")
    obj.selectDropDownOption("Reason Type", "Journal Entry")
    obj.selectRadioButton("USD")

#test1()

# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert 'h' in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, 'check')