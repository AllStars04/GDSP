from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import _multiprocessing
import psutil

from selenium.common.exceptions import TimeoutException
import Module.Utility
import datetime
import time
import Module.logger
import Module.CleanUp
import os
import getpass


class SeleniumBrowser:
    def __init__(self):
        self.browserType = Module.Utility.ReadDataFromJsonFile("tool", "browserType")
        self.timeout = Module.Utility.ReadDataFromJsonFile("tool", "timeout")
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/users/"+getpass.getuser()+"/AppData/Local/Google/Chrome/User Data/Default")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.get_input_type = Module.Utility.ReadDataFromJsonFile("tool", "configfile")
        self.dic = {}

    def __call__(self, *args, **kwargs):
        return self.driver

    def openUrl(self):
        # CHANGE get the URL from configuration file
        get_input_type = Module.Utility.ReadDataFromJsonFile("tool", "configfile")
        if get_input_type != "xls":
          url = Module.Utility.ReadDataFromJsonFile("sut", "url")
        elif get_input_type == "xls":
          Env = Module.Utility.fnReadDataFromExcel("Login.xlsx", "URL", "ToBeExecuted","Yes","Type")
          url = Module.Utility.fnReadDataFromExcel("Login.xlsx", "URL", "Type",Env,"URL")
        Module.logger.INFO("Opening URL " + url)
        self.driver.get(url)


    def login(self):
        get_input_type = Module.Utility.ReadDataFromJsonFile("tool", "configfile")
        if get_input_type != "xls":
          strUserName = Module.Utility.ReadDataFromJsonFile("Login", "Username")
          strPassword = Module.Utility.ReadDataFromJsonFile("Login", "Password")
        elif get_input_type == "xls":
           Env = Module.Utility.fnReadDataFromExcel("Login.xlsx", "URL", "ToBeExecuted", "Yes", "Type")
           strUserName = Module.Utility.fnReadDataFromExcel("Login.xlsx",Env, "TypeOfUser","Admin","UserName")
           strPassword = Module.Utility.fnReadDataFromExcel("Login.xlsx", Env, "TypeOfUser", "Admin","Password")
        self.driver.find_element_by_id("__ns2087359418_username").send_keys(strUserName)
        self.driver.find_element_by_id("__ns2087359418_password").send_keys(strPassword)
        self.driver.find_element_by_id("__ns2087359418_loginBtn").click()
        home = None
        local_timeout = 0
        while (home == None) and local_timeout < self.timeout / 2:
            try:
                home = self.driver.find_element_by_id("__ns1790630358_homeLnk2")
            except:
                Module.logger.WARNING("Login not complete")
                time.sleep(2)
                local_timeout = local_timeout + 1

        if home:
            Module.logger.INFO("Logged in with user: Home screen is visible")
            time.sleep(1)
        else:
            Module.logger.ERROR("Login not completed within " + self.timeout + " seconds")

    def gotodefaultframe(self):
        Module.logger.DEBUG("Switching to default content")
        self.driver.switch_to.default_content()

    def gotocorrectframe(self):
        all_iframe = self.driver.find_elements_by_tag_name("IFRAME")
        framefound = "false"
        if all_iframe == None:
            Module.logger.DEBUG("There is no child frame available, so assuming current frame is the correct one")
        else:
            for frame in all_iframe:
                if frame.get_attribute("id") != "" and frame.get_attribute("id") != "home_iframe":
                    Module.logger.DEBUG("Switching to frame : " + frame.get_attribute("id"))
                    self.driver.switch_to.frame(frame.get_attribute("id"))
                    framefound = "true"
                if framefound == "true":
                    break

    def ifpageloaded(self):
        loaded = "true"
        ##CHANGE Code to check if page is loaded successfully or not
        count = 0
        self.driver.find_elements_by_class_name("loading")
        while loaded == "true" and count < self.timeout:
            try:
                elem = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "preloader32"))
                )
            except:
                Module.logger.DEBUG("Exception in page loading")
                elem = None

            if elem != None and elem.is_displayed():
                Module.logger.DEBUG("Page is still loading, so waiting for page to load")
            else:
                Module.logger.DEBUG("Page loading is complete")
                loaded = "false"

            count = count + 1
            time.sleep(2)

    def getValueFromLabel(self,lblName):
        obj = self.driver.find_elements_by_tag_name("label")
        if obj!= None:
            for lblObj in obj:
                if lblObj.text == lblName:
                    span_obj = lblObj.find_elements_by_xpath("following::span")
                    Module.logger.INFO("The Value got from Label Name "+lblName+ " is :"+str(span_obj[0].text))
                    return span_obj[0].text
        else:
            Module.logger.ERROR("No Object Found for the Label "+ lblName)


    def logout(self):
        self.driver.find_element_by_id("__ns1790630358_logoutLnk").click()
        self.driver.close()
        Module.CleanUp.killAllProcess()

    def addValueToDic(self,valuetoStore,valueToAdd):
        self.dic.update({valuetoStore:valueToAdd})

    def compareTwoValues(self, value1, value2, operation):
        if operation.lower() == "equal":
            if self.dic.get(value1) == self.dic.get(value2):
               Module.logger.INFO("Both Values Match!!")
            else:
                Module.logger.ERROR("Values Dont Match!!")