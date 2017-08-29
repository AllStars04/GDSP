import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def enterText(driverObject,textName,textValue):

    if textName == None or textValue == None:
        Module.logger.ERROR("Button name not provided")
    success = 0
    obj = Module.getObject.getObjByRepo(driverObject,"text",textName)
    if obj != None:
        try:
            Module.logger.DEBUG("Clicking based on given parameters")
            obj.clear()
            obj.send_keys(textValue)
            success = 1
        except:
            Module.logger.ERROR("Exception in clicking using given locator and locator value")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"text",textName)
        if obj != None:
            try:
                next_obj = obj.find_element_by_xpath("following::input")
                try:
                    next_obj.clear()
                    next_obj.send_keys(textValue)
                except:
                    Module.logger.ERROR("Can't enter value for "+textName)
            except:
                Module.logger.ERROR("Can't find input box for "+textName)
        else:
            Module.logger.ERROR("No object found for text "+textName)

