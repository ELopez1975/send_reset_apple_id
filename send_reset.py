from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from load_page import page_is_loaded


class Reset(object):
    """Request a password reset for Apple ID from Apple multiple times."""

    url = "https://iforgot.apple.com/password/verify/appleid" #URL to reset apple id
    
    def __init__(self, apple_id, attemps=10, headless=False):
        self.apple_id = apple_id
        self.attemps = attemps
        self.headless = headless

        # if headless run selenium

        # if not headless run requests
