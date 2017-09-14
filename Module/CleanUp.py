import psutil
import Module.logger

def killProcessFromTaskManager(processName):
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == processName:
            try:
                proc.kill()
                break
            except:
                Module.logger.INFO("Process does not exist")

def killAllProcess():
    #Kill ChromeDriver and Chrome
    killProcessFromTaskManager("chromedriver.exe")
    killProcessFromTaskManager("chrome.exe")
