import Module.getObject
import Module.logger
import Module.Algorithms
import Module.Utility

def verifyTableColumnHeaders(driverObject,tableName,ColNamesList):
    counter = 0
    blnVerified = False
    obj = Module.getObject.getObjByRepo(driverObject, "table", tableName)
    if obj != None:
        ColNames = ColNamesList.split(',')
        for i in range(0, len(ColNames)):
            if ColNames[i] in obj[0].text:
                counter += 1
                if counter == len(ColNames)-1:
                    blnVerified = True
                    Module.logger.INFO("Table Headers Verified. The table actually contains the following Column Names " + obj[0].text)
        if blnVerified == False:
           Module.logger.ERROR("Table Headers Verified. The table does not contain the headers " + str(ColNames))
    else:
        Module.logger.ERROR("No object found for table " + tableName)

