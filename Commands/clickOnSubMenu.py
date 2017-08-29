import sys
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def clickOnSubmenu(driverObject,subMenuName):

    success = 0
    if subMenuName == None:
        Module.logger.ERROR("Sub Menu name not provided")

    obj = Module.getObject.getObjByRepo(driverObject,"submenu",subMenuName)
    if obj != None:
        try:
            obj.click()
            success = 1
        except:
            Module.logger.ERROR("Sub Menu "+subMenuName+ "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"submenu",subMenuName)
        if obj != None:
            try:
                obj.click()
            except:
                Module.logger.ERROR("Sub Menu " + subMenuName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for sub menu "+subMenuName)