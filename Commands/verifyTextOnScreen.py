import sys
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def verifyTextOnScreen(driverObject,textName):
    success = 0
    if textName == None:
        Module.logger.ERROR("Text to search not provided")
    obj = Module.getObject.getObjByRepo(driverObject, "statictext", textName)
    if obj != None:
     for divObj in obj:
         if divObj.text == textName:
            Module.logger.INFO("Static Text Found : "+  textName)
            success = 1
            break
    else:
        Module.logger.INFO("Object " + textName + " is not found in Repository")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"statictext",textName)
        if obj != None:
            Module.logger.INFO("Static Text Found : " + textName)
            success = 1
        else:
            Module.logger.ERROR("Text Not found : "+textName)



