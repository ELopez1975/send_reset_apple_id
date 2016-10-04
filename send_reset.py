from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from load_page import page_is_loaded
import argparse


class Reset(object):
    """Request a password reset for Apple ID from Apple multiple times."""

    url = "https://iforgot.apple.com/password/verify/appleid" #URL to reset apple id
    
    def __init__(self, apple_id, count=10, headless=False):
        self.apple_id = apple_id
        self.count = count
        self.headless = headless

        if self.headless == True:
            self.use_requests()
        else:
            self.use_selenium()


    def use_selenium(self):
        count_down = 0

        driver = webdriver.Firefox()
        driver.get(self.url)

        while count_down < self.count:

            #driver = webdriver.Firefox()
            #driver.get(self.url)

            #wait = ui.WebDriverWait(driver, 10)
            #wait.until(page_is_loaded)

	    # input apple id into search field
            elem = driver.find_element_by_xpath("//input[@id='appleid']")
            elem.send_keys(self.apple_id)
            elem.send_keys(Keys.RETURN)

            #wait = ui.WebDriverWait(driver, 10)
            #wait.until(page_is_loaded)
            sleep(2)
            # Selecting to reset password
            #elem2 = driver.find_element_by_xpath("//div[@class='text-centered']/div[@class='btn-group flow-controls']/button[@id='action']")
            elem2 = driver.find_element_by_id("action")
            elem2.click()

            #wait = ui.WebDriverWait(driver, 10)
            #wait.until(page_is_loaded)
            sleep(2)
            # Select to get an email
            #elem3 = driver.find_element_by_xpath("//button[@class='btn blue-btn btn-link iforgot-btn done link']")
            elem3 = driver.find_element_by_id("action")
            elem3.click()
            sleep(2)
            # Select Done
            elem4 = driver.find_element_by_class_name("done")
            elem4.click()

            count_down += 1
            print ("Attempt %d done" % count_down)
            sleep(2)

        sleep(2)
        driver.quit()

    def use_requests(self):
        pass



parser = argparse.ArgumentParser(description="Send one or more requests to reset Apple ID")
parser.add_argument("AppleID", action="store")
parser.add_argument("--count", type=int, default=10)
parser.add_argument("--headless", default=False)

results = parser.parse_args()

reset = Reset(results.AppleID, results.count, results.headless)

#if __name__ == "__main__":    
    #    test = Reset("test@test.test", attemps=2)
