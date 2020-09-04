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
    def __init__(self, browser, display, login, password): 
        self.browser = browser
        self.display = display
        self.login = login 
        self.password = password

    def run(self, base_url, users): 
        self.browser.get(base_url)
        try:
            # This is just an example scenario
            pyautogui.screenshot('/home/agent/screenshots/1.png')       
            usernameInput = self.browser.find_element_by_id("usernamefld")
            usernameInput.clear()
            usernameInput.send_keys(self.login)
            pyautogui.screenshot('/home/agent/screenshots/1.png')
            passowrdInput = self.browser.find_element_by_id("passwordfld")
            passowrdInput.clear()
            passowrdInput.send_keys(self.password)
            pyautogui.screenshot('/home/agent/screenshots/3.png')
            loginBtn = self.browser.find_element_by_name("login")
            loginBtn.click()

        except TimeoutException as timeout:
            print(timeout)
            self.browser.quit()
            self.display.stop()
            sys.exit(1)
        finally: 
            self.browser.quit()
            self.display.stop()
