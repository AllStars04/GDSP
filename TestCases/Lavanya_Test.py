import Class.Automation

obj = Class.Automation.Automation()
obj.openURL()
obj.login()
obj.clickOnLink("Administration")
obj.clickOnLink("Provisioning profiles")
obj.verifyTextOnScreen("Provisioning profiles")
obj.enterText("Provisioning profile","Autotest2")
obj.clickOnButton("Search")
obj.clickOnLink("Autotest2")
obj.verifyTextOnScreen("Configuration")
obj.clickOnButton("ConfigEdit")
obj.selectDropDownOption("APN","apn1")
obj.clickOnButton("Save")
obj.verifyTextOnScreen("Settings successfully updated")


