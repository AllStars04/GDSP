import sys
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def clickOnMenu(driverObject,menuName):

    success = 0
    if menuName == None:
        Module.logger.ERROR("Menu name not provided")

    obj = Module.getObject.getObjByRepo(driverObject,"menu",menuName)
    if obj != None:
        try:
            obj.click()
            success = 1
        except:
            Module.logger.ERROR("Menu "+menuName+ "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"menu",menuName)
        if obj != None:
            try:
                obj.click()
            except:
                Module.logger.ERROR("Menu " + menuName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for menu "+menuName)