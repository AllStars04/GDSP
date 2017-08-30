import Class.Automation

obj = Class.Automation.Automation()
obj.openURL()
obj.login()
obj.clickOnLink("Administration")
obj.clickOnLink("Service profiles")
obj.verifyTextOnScreen("Service profiles")
obj.selectDropDownOption("ServiceProfOrganisation","CARGOTEC")
obj.clickOnButton("Search")
obj.verifyTextOnScreen("matching result")
print("SUCCESS : Operator is able to search service profile for organization")
obj.clickOnLink("Clear fields")
obj.logout()