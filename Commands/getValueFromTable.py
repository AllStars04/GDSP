import Module.getObject
import Module.logger
import Module.Algorithms
import Module.Utility
import Class.Automation

def getValueFromTable(self):
    counter = 0
    blnVerified = False
    col_dic = {}
    all_table = self.driver.find_elements_by_tag_name("table")
    for tab in all_table:
        table_class_name = tab.get_attribute("class")
        if table_class_name != "":
            elem = tab
            break

    all_cols = elem.find_elements_by_tag_name("th")
    col_index = 0
    for col in all_cols:
        col_index = col_index+1
        key = col_index
        value = col.text
        col_dic.update({key:value})

    Module.logger.INFO(col_dic)
    # if obj != None:
    #     ColNames = ColNamesList.split(',')
    #     for i in range(0, len(ColNames)):
    #         if ColNames[i] in obj[0].text:
    #             counter += 1
    #             if counter == len(ColNames)-1:
    #                 blnVerified = True
    #                 Module.logger.INFO("Table Headers Verified. The table actually contains the following Column Names " + obj[0].text)
    #     if blnVerified == False:
    #        Module.logger.ERROR("Table Headers Verified. The table does not contain the headers " + str(ColNames))
    # else:
    #     Module.logger.ERROR("No object found for table " + tableName)

