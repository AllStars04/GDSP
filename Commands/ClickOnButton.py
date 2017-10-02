import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject
import Module.CleanUp
import Class.UserDefinedException


def clickOnButton(driverObject,buttonName):
    #Report = Class.Report.Report()
    Excep = Class.UserDefinedException.UserDefinedException()
    success = 0
    if buttonName == None:
        Module.logger.ERROR("Button name not provided")
    obj = Module.getObject.getObjByRepo(driverObject,"button",buttonName)
    if obj != None:
        try:
            obj.click()
            Module.logger.INFO("Button" + buttonName + " is clicked")
            success = 1
        except:
            Module.logger.ERROR("Button "+buttonName+ "is not clickable")
    else:
        Module.logger.INFO("Object " +buttonName+" is not found in Repository")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"button",buttonName)
        if obj != None:
            try:
                obj.click()
                Module.logger.INFO("Button" + buttonName + " is clicked")
            except:
                # Clean up before raising exception
                Module.CleanUp.killAllProcess()
                Excep.raiseException("Button with name "+buttonName+" is not clickable")
        else:
            Module.logger.ERROR("No Object found for button "+buttonName)











