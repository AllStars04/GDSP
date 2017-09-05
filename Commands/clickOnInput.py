import sys
import Class.SeleniumBrowser
import Module.Algorithms
import Module.Utility
import Module.logger
import Module.getObject

def clickOnInput(driverObject,inputName):

    success = 0
    if inputName == None:
        Module.logger.ERROR("Input name not provided")


    obj = Module.getObject.getObjByRepo(driverObject,"input",inputName)
    if obj != None:
        try:
            obj.click()
            success = 1
        except:
            Module.logger.ERROR("Input "+inputName+ "is not clickable")

    if success == 0:
        obj = Module.getObject.getObjByAlgo(driverObject,"input",inputName)
        if obj != None:
            try:
                obj.click()
                #success = 1
                #input_obj = obj.find_elements_by_tag_name("input")
                #if input_obj != None:
                    #for iobj in input_obj:
                      #  if iobj.text == inputName:
                      #      Module.logger.DEBUG("During search we found the object with attribute text: " + iobj.text)
                      #      found = "true"
                     #   if found == "true":
                           # break
                 #   if found == "true":
                 #       iobj.click()
                #    else:
                #        Module.logger.ERROR("Object with given value " + inputName+ " not found")
            except:
                Module.logger.ERROR("INPUT " + inputName + "is not clickable")
        else:
            Module.logger.ERROR("No Object found for input "+inputName)











