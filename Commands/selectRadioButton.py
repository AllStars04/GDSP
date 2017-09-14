import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject
import Module.CleanUp
import Class.UserDefinedException
import time

def selectRadioButton(driverObject,radbtnName):
    Excep = Class.UserDefinedException.UserDefinedException()
    success =0
    if radbtnName == None:
        Module.logger.ERROR("Radio Button name is not provided")
    #Get Object From Repository
    obj = Module.getObject.getObjByRepo(driverObject,"radiobutton",radbtnName)
    if (obj!= None):
     try:
         obj.Click()
         Module.logger.INFO("Radio Button " + radbtnName + " is selected")
         success = 1
     except:
         Module.logger.ERROR("Radio Button " + radbtnName + "is not clickable")
    else:
        Module.logger.INFO("Object " + radbtnName + " is not found in Repository")

    if success == 0:
       #Get Object By Dynamic Algorithm
       obj = Module.getObject.getObjByAlgo(driverObject,"radiobutton",radbtnName)
       if obj != None:
           try:
               obj.click()
               Module.logger.INFO("Radio Button " + radbtnName + " is selected")
           except:
               Module.CleanUp.killAllProcess()
               Excep.raiseException("Radio Button " + radbtnName + "is not clickable")
       else:
           Module.logger.ERROR("No Object found for radio button " + radbtnName)

