import os
from time import sleep
import shutil
import sys 
import os.path
import Xlib.display
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import pyautogui
import glob

pyautogui.FAILSAFE = False

class ExecutionPlan: 
    def __init__(self, browser, display, login, password, downloads_dir, screenshots_dir): 
        self.browser = browser
        self.display = display
        self.login = login 
        self.password = password
        self.downloads_dir = downloads_dir
        self.screenshots_dir = screenshots_dir

    def run(self, base_url): 
        self.browser.get(base_url)
        try:
            # This is just an example scenario
            pyautogui.screenshot("{}/1.png".format(self.screenshots_dir))       
            sleep(5)

        except TimeoutException as timeout:
            print(timeout)
            self.browser.quit()
            self.display.stop()
            sys.exit(1)
        finally: 
            self.browser.quit()
            self.display.stop()
