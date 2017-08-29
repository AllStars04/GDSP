import Module.Utility
import Module.Algorithms
import Module.logger

def getObjByRepo(driverObject,type,name):
    idtype, idvalue = Module.Utility.CheckIfDefinedElementExistInRepo(type, name)
    if idtype != None and idvalue != None:
        Module.logger.INFO("ID Type for " +type+ " " +name+ " is " + idtype)
        Module.logger.INFO("Value for " + type + " " + name + " is " + idvalue)
        return Module.Algorithms.find_obj_using_config(driverObject,idtype, idvalue)
    else:
        return None

def getObjByAlgo(driverObject,type,name):
    Module.logger.DEBUG("Getting locator and locator value for "+type)
    locator, locatorvalue = Module.Utility.getDataForDynamicAlgo(type)
    if locator != None and locatorvalue != None:
        Module.logger.INFO("LOCATOR: "+locator+ ", locatorvalue: " +locatorvalue+ ", value: "+name)
        return Module.Algorithms.find_auto_element(driverObject,locator, locatorvalue, name)
    else:
        Module.logger.ERROR("locator and locator value not provided in config file")
        return None

