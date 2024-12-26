from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from enum import Enum
import time
from datetime import datetime

class DelayTimes(Enum):
    DELAY_0 = 0
    DELAY_10 = 10
    DELAY_20 = 20
    DELAY_30 = 30
    DELAY_60 = 60
    DELAY_MIN = 10
    DELAY_MAX = 100
    DELAY_MEDIUM = 50

class BrowserTypes(Enum):
    CHROME = 0
    FIREFOX = 1
    EDGE = 2

class Automator:
    def __init__(self, browser : BrowserTypes,  initial_url : str):
        if browser == BrowserTypes.CHROME:
            self.__driver = webdriver.Chrome()
        elif browser == BrowserTypes.FIREFOX:
            self.__driver = webdriver.Firefox()
        elif browser == BrowserTypes.EDGE:
            self.__driver = webdriver.Edge()
        else:  
            self.__driver = webdriver.Edge() #default to edge
        self.__driver.get(initial_url)
        self.__driver.maximize_window()
        self.__title = self.__driver.title
        self.__delay_afer_action = 0
        self.__browserType = browser
        self.__url = initial_url


    def set_window_size(self, width, height):
        self.__driver.set_window_size(width, height)
    
    def maximize_window(self):
        self.__driver.maximize_window()
    
    def minimize_window(self):
        self.__driver.minimize_window()
    
    def normal_window(self):
        self.__driver.normal_window()  

    def set_url(self, url):
        self.__driver.get(url) 

    def set_speed(self, speed):
        self.__delay_after_action = speed

    def show_popup(self, message):
        self.__driver.execute_script("alert('"+message+"');")
  
    def close_browser(self):
        self.__driver.quit()

    def attach_to_existing_browser(self, driver):
        self.__driver = driver  

    def fixed_delay(self, delay):
        time.sleep(delay)

    def take_screenshot(self, path):
        self.__driver.save_screenshot(path) 

    def get_xpath_element(self, xpathOfElement,timeOutLimit):
        # Wait until a specific element is visible on the page
        try:
            element = WebDriverWait(self.__driver, timeOutLimit).until(
                EC.visibility_of_element_located((By.XPATH, xpathOfElement))
            )
            time.sleep(self.__delay_after_action)
            return element
        except TimeoutException:
            print("Element was not found within the time frame")
            time.sleep(self.__delay_after_action)
            return None

    def send_keys_to_xpath_element(self, xpathOfElement, timeOutLimit, keyStrokes):
        element = self.get_xpath_element(xpathOfElement,timeOutLimit)
        if element is not None:
            element.send_keys(keyStrokes)
            time.sleep(self.__delay_after_action)
        else:
            time.sleep(self.__delay_after_action)
            self.__raise_and_log_exception("Error....failed to identify element of xpath " + xpathOfElement)
        
    def send_click_to_xpath_element(self, xpathOfElement, timeOutLimit):
        element = self.get_xpath_element(xpathOfElement,timeOutLimit)
        if element is not None:
            element.click()
            time.sleep(self.__delay_after_action)
        else:
            time.sleep(self.__delay_after_action)
            self.__raise_and_log_exception("Error....failed to identify element of xpath " + xpathOfElement)
        
    def get_text_of_xpath_element(self, xpathOfElement, timeOutLimit):
        element = self.get_xpath_element(xpathOfElement,timeOutLimit)
        if element is not None:
            time.sleep(self.__delay_after_action)
            return element.text
        else:
            time.sleep(self.__delay_after_action)
            self.__raise_and_log_exception("Error....failed to identify element of xpath " + xpathOfElement)

    def __raise_and_log_exception(self, message):
        # Get the current timestamp
        current_time = datetime.now()
        # Format the timestamp
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        message = f"{formatted_time} :: {message}"
        raise ValueError(message)



