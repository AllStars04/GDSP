import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def clickOnLink(driverObject,lnkName):
    success = 0
    if lnkName == None:
        Module.logger.ERROR("Link name not provided")

    obj = Module.getObject.getObjByRepo(driverObject,"link",lnkName)
    if obj != None:
     for lnkObj in obj:
         if lnkObj.text == lnkName:
            try:
                lnkObj.click()
                print("Object Found From Repo")
                success = 1
                break
            except:
                Module.logger.ERROR("Link "+lnkName+ "is not clickable")
    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"link",lnkName)
        if obj != None:
            try:
                obj.click()
                print("Object Found By Dynamic Algo")
            except:
                Module.logger.ERROR("Link " + lnkName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for link "+lnkName)
