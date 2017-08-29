import sys
import Module.Algorithms
import Module.Utility
import Module.logger

def selectDropDownOption(driverObject,dropDownName,optionValue):
    success = 0
    if dropDownName == None or optionValue == None:
        Module.logger.ERROR("Drop down name or option not provided")
    obj = Module.getObject.getObjByRepo(driverObject,"dropdown", dropDownName)
    if obj!= None:
        drop_down_elements = obj.find_elements_by_tag_name("option")
        if len(drop_down_elements) > 0:
            for elem in drop_down_elements:
                if elem.text == optionValue:
                    try:
                       elem.click()
                       print("Object Found From Repo")
                       success = 1
                       break
                    except:
                       Module.logger.ERROR("DropDown " + dropDownName + "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"dropdown",optionValue)
        if obj != None:
            try:
                obj.click()
                print("Object Found By Dynamic Algo")
            except:
                Module.logger.ERROR("DropDown " + dropDownName + "is not clickable")
        else:
          Module.logger.ERROR("No Object found for dropdown " + dropDownName)
