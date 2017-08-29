import sys
import Module.Algorithms
import Module.Utility

def verifyTextOnScreen(self,textName):

    if textName == None:
        Module.logger.ERROR("Text to search not provided")
    else:
        if self.driver.page_source.__contains__(textName):
            Module.logger.DEBUG("Text present in web page")
        else:
            Module.logger.ERROR("Text "+textName+" not present in web page")


