import selenium
##from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.keys import Keys
import time

browser = selenium.webdriver.Firefox() # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page
assert browser.title == "Yahoo!"
elem = browser.find_element_by_name("p") # Find the query box
elem.send_keys("selenium" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()