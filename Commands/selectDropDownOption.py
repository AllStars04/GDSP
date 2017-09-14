import sys
import Module.Algorithms
import Module.Utility
import Module.logger
import Commands.enterText
import Module.getObject
import Module.CleanUp
import Class.UserDefinedException

def selectDropDownOption(driverObject,dropDownName,optionValue):
    Excep = Class.UserDefinedException.UserDefinedException()
    success = 0

    if dropDownName == None or optionValue == None:
        Module.logger.ERROR("Drop down name or option not provided")
    tempobj = Module.getObject.getObjByRepo(driverObject, "dropdown", dropDownName)
    if tempobj != None:
        try:
            tempobj1 = tempobj.find_elements_by_xpath("following::div")
            try:
                tempobj1[0].click()
                try:
                    obj1 = tempobj.find_elements_by_xpath("//li[@class = 'active-result']")
                    for obj in obj1:
                        if obj.text == optionValue:
                            try:
                                obj.click()
                                Module.logger.INFO("Drop Down Found. Selecting option  " + optionValue + " for the dropdown " + dropDownName)
                                break
                            except:
                                Module.logger.ERROR("DropDown " + dropDownName + "is not clickable")
                except:
                    Module.logger.ERROR("No object found for the link")
            except:
                Module.logger.ERROR("Drop Down "+dropDownName+" is not clickable")
        except:
            Module.logger.ERROR("Div Element Not Found")
    else:
        Module.logger.INFO("Object " +dropDownName+" is not found in Repository")

    if success == 0:
        tempobj = Module.getObject.getObjByAlgo(driverObject, "dropdown", dropDownName)
        if tempobj != None:
            try:
                tempobj1 = tempobj.find_elements_by_xpath("following::div")
                try:
                    tempobj1[0].click()
                    try:
                        obj1 = tempobj.find_elements_by_xpath("//li[@class = 'active-result']")
                        for obj in obj1:
                            if obj.text == optionValue:
                                try:
                                    obj.click()
                                    Module.logger.INFO("Drop Down Found. Selecting option  " + optionValue + " for the dropdown " + dropDownName)
                                    break
                                except:
                                    Module.CleanUp.killAllProcess()
                                    Excep.raiseException("DropDown " + dropDownName + "is not clickable")
                    except:
                        Module.CleanUp.killAllProcess()
                        Excep.raiseException("No object found for the link")
                except:
                    Module.CleanUp.killAllProcess()
                    Excep.raiseException("Drop Down " + dropDownName + " is not clickable")
            except:
                Module.CleanUp.killAllProcess()
                Excep.raiseException("Div Element Not Found")
        else:
            Module.logger.ERROR("No object found for drop down " + dropDownName)

