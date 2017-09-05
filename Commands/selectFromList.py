import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def selectFromList(driverObject,optionName):

    success = 0
    if optionName == None:
        Module.logger.ERROR("Option name not provided")


    obj = Module.getObject.getObjByRepo(driverObject,"list",optionName)
    if obj != None:
        try:
            obj.click()
            success = 1
        except:
            Module.logger.ERROR("Option "+optionName+ "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"list",optionName)
        if obj != None:
            try:
                obj.click()
            except:
                Module.logger.ERROR("option " + optionName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for option "+optionName)











