import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject
import Module.CleanUp
import Class.UserDefinedException
import time

def clickOnInput(driverObject,inputName,inputValue):
    Excep = Class.UserDefinedException.UserDefinedException()
    success = 0
    if inputName == None:
        Module.logger.ERROR("Input name not provided")
    all_obj = Module.getObject.getObjByRepo(driverObject,"input",inputName)
    if all_obj != None:
     for obj in all_obj:
        if inputName in obj.text:
            try:
                obj.click()
                try:
                    input_obj = obj.find_element_by_xpath("//input[contains(@id,'TreeOrganisationInput')]")
                    input_obj.clear()
                    input_obj.send_keys(inputValue)
                    time.sleep(10)
                except:
                    Module.logger.ERROR("Cannot enter value in the input field " + inputName)
                try:
                    actualObj = input_obj.find_elements_by_xpath("//li[contains(@class,'search-result')]")
                    actualObj[0].click()
                    Module.logger.INFO("INPUT " + inputName + " is selected")
                    success = 1
                    break
                except:
                    Module.logger.ERROR("Cannot select value from the list " + inputName)
            except:
                Module.logger.ERROR("Cannot click on input field " + inputName)
        else:
            Module.logger.ERROR("No object found for input "+inputName)
    else:
         Module.logger.INFO("Object " +inputValue+" is not found in Repository")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"input",inputName)
        if obj != None:
            try:
                obj.click()
                try:
                    input_obj = obj.find_element_by_xpath("//input[contains(@id,'TreeOrganisationInput')]")
                    input_obj.clear()
                    input_obj.send_keys(inputValue)
                    time.sleep(10)
                except:
                    Module.CleanUp.killAllProcess()
                    Excep.raiseException("Exception in entering value in the input field " + inputName)
                try:
                    actualObj = input_obj.find_elements_by_xpath("//li[contains(@class,'search-result')]")
                    actualObj[0].click()
                    Module.logger.INFO("INPUT " + inputName + " is selected")
                    success = 1
                except:
                    Module.CleanUp.killAllProcess()
                    Excep.raiseException("Exception in  selecting value from the list " + inputName)
            except:
                # Clean up before raising exception
                Module.CleanUp.killAllProcess()
                Excep.raiseException("Input field " + inputName+" is not clickable")
        else:
            Module.logger.ERROR("No Object found for input "+inputName)











