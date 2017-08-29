import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def clickOnButton(driverObject,buttonName):

    success = 0
    if buttonName == None:
        Module.logger.ERROR("Button name not provided")


    obj = Module.getObject.getObjByRepo(driverObject,"button",buttonName)
    if obj != None:
        try:
            obj.click()
            success = 1
        except:
            Module.logger.ERROR("Button "+buttonName+ "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"button",buttonName)
        if obj != None:
            try:
                obj.click()
            except:
                Module.logger.ERROR("Button " + buttonName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for button "+buttonName)











