import Class.Automation

obj = Class.Automation.Automation()
obj.openURL()
obj.login()
obj.clickOnLink("Administration")
obj.clickOnLink("Service profiles")
obj.verifyTextOnScreen("Service profiles")
##Drop Down Implementation Pending!!!!!
#obj.selectDropDownOption("ServiceProfOrganisation","CARGOTEC")
ServiceProf1 = obj.getValueFromLabel("Service Profile")
obj.enterText("Service Profile","BMW_IT")
obj.clickOnButton("Search")
obj.verifyTextOnScreen("matching result")
print("SUCCESS : Operator is able to search service profile for organization")
obj.clickOnLink("Clear fields")
ServiceProf2 = obj.getValueFromLabel("Service Profile")
if ServiceProf1 == ServiceProf2:
    print("SUCCESS")
obj.logout()
#Lavanya