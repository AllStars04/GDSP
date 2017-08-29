import Class.SeleniumBrowser
import Module.logger
#import Module.Reports
import Commands.ClickOnButton
import Commands.clickOnMenu
import Commands.clickOnSubMenu
import Commands.enterText
import Commands.selectDropDownOption
import Commands.verifyTextOnScreen
import Commands.clickOnLink
import Commands.clickOnImage
import Commands.selectRadioButton


class Automation:
    def __init__(self) -> object:
        self.driver = Class.SeleniumBrowser.SeleniumBrowser()
        self.driver()

    def openURL(self):
        self.driver.openUrl()

    def login(self):
        self.driver.login()

    def performPreChecks(self):
        self.driver.ifpageloaded()
        #self.driver.gotocorrectframe()

    def clickOnButton(self,buttonName):
        Module.logger.INFO("Clicking on button: "+buttonName)
        self.buttonName = buttonName
        self.performPreChecks()
        Commands.ClickOnButton.clickOnButton(self.driver, buttonName)
        # tempObj = Class.clickOnButtonT.clickOnButton(self.driver,buttonName)
        # tempObj(self.driver,buttonName)

    def clickOnMenu(self,menuName):
        Module.logger.INFO("Clicking on menu: "+menuName)
        #Module.Reports.allure_test()
        self.menuName = menuName
        self.performPreChecks()
        self.driver.gotodefaultframe()
        Commands.clickOnMenu.clickOnMenu(self.driver, menuName)

    def clickOnSubmeu(self,subMenuName):
        Module.logger.INFO("Clicking on submenu: "+subMenuName)
        self.subMenuName = subMenuName
        self.performPreChecks()
        self.driver.gotodefaultframe()
        Commands.clickOnSubMenu.clickOnSubmenu(self.driver, subMenuName)

    def enterText(self,textName,textValue):
        Module.logger.INFO("Entering text "+textValue+ " for "+textName)
        self.textName = textName
        self.textValue = textValue
        self.performPreChecks()
        Commands.enterText.enterText(self.driver, textName, textValue)

    def selectDropDownOption(self,menuName,optionName):
        Module.logger.INFO("Selecting dropdown menu: "+menuName+ " and option "+optionName)
        self.menuName = menuName
        self.optionName = optionName
        self.performPreChecks()
        Commands.selectDropDownOption.selectDropDownOption(self.driver, menuName, optionName)

    def verifyTextOnScreen(self,textName):
        Module.logger.INFO("Verifying if text: "+textName+ " is present on page")
        self.textName = textName
        self.performPreChecks()
        Commands.verifyTextOnScreen.verifyTextOnScreen(self.driver, textName)

    def clickOnLink(self,lnkName):
        Module.logger.INFO("Clicking on link: " + lnkName)
        self.lnkName = lnkName
        self.performPreChecks()
        Commands.clickOnLink.clickOnLink(self.driver, lnkName)

    def clickOnImage(self,imgName):
        Module.logger.INFO("Clicking on Image: " + imgName)
        self.imgName = imgName
        self.performPreChecks()
        Commands.clickOnImage.clickOnImage(self.driver, imgName)

    def selectRadioButton(self, radbtnName):
        Module.logger.INFO("Clicking on Radio Button : " + radbtnName)
        self.radbtnName = radbtnName
        self.performPreChecks()
        Commands.selectRadioButton.selectRadioButton(self.driver, radbtnName)








