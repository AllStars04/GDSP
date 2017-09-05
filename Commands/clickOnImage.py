import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def clickOnImage(driverObject,imgName):
    success = 0
    if imgName == None:
        Module.logger.ERROR("Image name not provided")

    obj = Module.getObject.getObjByRepo(driverObject,"image",imgName)
    if obj != None:
     for ImgObj in obj:
         if imgName in ImgObj.get_attribute("src"):
            try:
                imgName.click()
                Module.logger.Info("Image " + imgName + " is selected")
                success = 1
                break
            except:
                Module.logger.ERROR("Image "+imgName+ "is not clickable")
    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"image",imgName)
        if obj != None:
            try:
                obj.click()
                Module.logger.Info("Image " + imgName + " is selected")
            except:
                Module.logger.ERROR("Image " + imgName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for image "+imgName)
