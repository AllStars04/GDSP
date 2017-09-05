import sys
import Module.Algorithms
import Module.Utility
import Module.logger
import Commands.enterText
import Class.SeleniumBrowser

def selectDropDownOption(driverObject,dropDownName,optionValue):
    success = 0
    if dropDownName == None or optionValue == None:
        Module.logger.ERROR("Drop down name or option not provided")
    ## Get Value from Repo for Drop Down - Not Implemented ##
    obj = Module.getObject.getObjByRepo(driverObject,"dropdown", dropDownName)
    if obj!= None:
        obj.click()
        Commands.enterText.enterText(driverObject, dropDownName, optionValue)
        drop_down_elements = obj.find_elements_by_tag_name("li")
        if len(drop_down_elements) > 0:
            for elem in drop_down_elements:
                if elem.text == optionValue:
                    try:
                       elem.click()
                       Module.logger.Info("Drop Down " + dropDownName + "  is selected with option : "+optionValue)
                       success = 1
                       break
                    except:
                       Module.logger.ERROR("DropDown " + dropDownName + "is not clickable")
    if success == 0:
        tempobj = Module.getObject.getObjByAlgo(driverObject, "dropdown", dropDownName)
        if tempobj!= None:
            # tempobj1 = tempobj.find_elements_by_xpath("following::div")
            # tempobj1[0].click()
            obj1 = tempobj.find_elements_by_xpath("//*[@class = 'chosen-results']/following::li")
            for obj in obj1:
                if obj.text == optionValue:
                    try:
                        obj.click()
                        Module.logger.INFO("Drop Down Found. Selecting option  "+optionValue+ " for the dropdown "+dropDownName)
                    except:
                        Module.logger.ERROR("DropDown " + dropDownName + "is not clickable")

