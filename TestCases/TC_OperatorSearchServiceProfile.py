import Class.Automation
import time
import Class.Report
import os

obj = Class.Automation.Automation()
Report = Class.Report.Report()
#Get the test case name
testCaseName = os.path.basename(__file__)
Report.createTestReport(testCaseName)
obj.openURL()
obj.login()
time.sleep(10)
obj.clickOnLink("Tools")
Report.Info("Clicked on the Link")
Report.Success("Clicked on the link")
# time.sleep(20)
#obj.selectCheckBox("Directly under only")
# obj.selectDropDownOption("Assignee","vftest@marcodegier.nl")
#obj.selectDropDownOption("Creator","aditi.aggarwal1@vodafone.com")
# obj.enterDate("Created","2017-07-01")
# obj.enterDate("and","2017-07-10")
#obj.logout()
#obj.clickOnInput("Organisation","VF-APAC")
# obj.clickOnLink("Store")
# obj.clickOnLink("All products")
# obj.verifyTextOnScreen("Catalogue")
# obj.clickOnButton("Search")
# obj.clickOnLink("111110001000000")
# obj.clickOnLink("History")
#obj.enterDate("Withdraw Date (UTC)","2017-07-01")
# obj.selectRadioButton("Activity list")
# obj.clickOnInput("Organisation","VF-APAC")


# ##Drop Down Implementation Pending!!!!!
# #obj.selectDropDownOption("ServiceProfOrganisation","CARGOTEC")
# ServiceProf1 = obj.getValueFromLabel("Service Profile")
# obj.enterText("Service Profile","BMW_IT")
# obj.clickOnButton("Search")
# obj.verifyTextOnScreen("matching result")
# print("SUCCESS : Operator is able to search service profile for organization")
# obj.clickOnLink("Clear fields")
# ServiceProf2 = obj.getValueFromLabel("Service Profile")
# if ServiceProf1 == ServiceProf2:
#     print("SUCCESS")
# obj.logout()
#Lavanya