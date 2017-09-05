import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def enterTextArea(driverObject,textAreaName,textAreaValue):

    if textAreaName == None or textAreaValue == None:
        Module.logger.ERROR("Button name not provided")
    success = 0
    obj = Module.getObject.getObjByRepo(driverObject,"textarea",textAreaName)
    if obj != None:
        try:
            Module.logger.INFO("Finding Element based on given parameters")
            obj.clear()
            obj.send_keys(textAreaValue)
            Module.logger.INFO("Text Area " + textAreaName + "  is entered with text : "+textAreaValue)
            success = 1
        except:
            Module.logger.ERROR("Exception in entering value in text area using given locator and locator value")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"textarea",textAreaName)
        if obj != None:
            try:
                next_obj = obj.find_element_by_xpath("following::input")
                try:
                    next_obj.clear()
                    next_obj.send_keys(textAreaValue)
                    Module.logger.INFO("Text Area " + textAreaName + "  is entered with text : " + textAreaValue)
                except:
                    Module.logger.ERROR("Can't enter value for "+textAreaName)
            except:
                Module.logger.ERROR("Can't find input box for "+textAreaName)
        else:
            Module.logger.ERROR("No object found for text area "+textAreaName)

