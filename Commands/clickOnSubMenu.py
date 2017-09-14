import sys
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject
import Module.CleanUp
import Class.UserDefinedException

def clickOnSubmenu(driverObject,subMenuName):
    Excep = Class.UserDefinedException.UserDefinedException()
    success = 0
    if subMenuName == None:
        Module.logger.ERROR("Sub Menu name not provided")

    obj = Module.getObject.getObjByRepo(driverObject,"submenu",subMenuName)
    if obj != None:
        try:
            obj.click()
            Module.logger.INFO("Sub-menu" + subMenuName + " is clicked")
            success = 1
        except:
            Module.logger.ERROR("Sub Menu "+subMenuName+ "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"submenu",subMenuName)
        if obj != None:
            try:
                obj.click()
                Module.logger.INFO("Sub-menu" + subMenuName + " is clicked")
            except:
                # Clean up before raising exception
                Module.CleanUp.killAllProcess()
                Excep.raiseException("Sub Menu " + subMenuName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for sub menu "+subMenuName)