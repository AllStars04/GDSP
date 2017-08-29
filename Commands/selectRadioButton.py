import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject
import time


def selectRadioButton(driverObject,radbtnName):
    success =0
    if radbtnName == None:
        Module.logger.ERROR("Radio Button name is not provided")
    #Get Object From Repository
    obj = Module.getObject.getObjByRepo(driverObject,"radiobutton",radbtnName)
    if (obj!= None):
     try:
         obj.Click()
         Module.logger.Info("Radio Button " + radbtnName + " is selected")
         print("Object Found From Repo")
         success = 1
     except:
         Module.logger.ERROR("Radio Button " + radbtnName + "is not clickable")
    if success == 0:
       #Get Object By Dynamic Algorithm
       obj = Module.getObject.getObjByAlgo(driverObject,"radiobutton",radbtnName)
       if obj != None:
           try:
               time.sleep(5)
               obj.click()
               Module.logger.Info("Radio Button " + radbtnName + " is selected")
               print("Object Found By Dynamic Algo")
           except:
               Module.logger.ERROR("Radio Button " + radbtnName + "is not clickable")
       else:
           Module.logger.ERROR("No Object found for radio button " + radbtnName)

