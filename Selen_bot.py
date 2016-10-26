import base64
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # Mouse actions and touchpad

#Variables
website = ''
url = ''
Chromedriver = 'C:\Users\Deaunna\Documents\chromedriver_win32\chromedriver'
link = 'Login'
local_mode = 0
Internet_mode = 1


def open_browser():
 try:
# Instantiate Chrome object
    driver = webdriver.Chrome(Chromedriver)
#Instantiate Action object for clicking, dragging etc..
    actions = ActionChains(driver)
# Navigate to a website
    driver.get(str(website))
# Halt program for a while
    time.sleep(6)
# Specify how html element will be accessed and store in variable
    element = driver.find_element_by_link_text(link)
# Start 'Actions' Queue, and dequeue(execute) each action on webpage
    actions.move_to_element(element).click(element).perform()
# Store site login information within variables
    username = base64.b64decode('Zm9yZC5qZXJlbXk1MTBAZ21haWwuY29t')
    password = base64.b64decode('Zm9yZC5qZXJlbXk1MTBAZ21haWwuY29t')
# Kill the process
    driver.quit()
 except Exception:
    print 'Something is wrong with chromdriver'
#If the code doesn't work exit interpreter
 sys.exit()
    


if __name__ == '__main__':
# Call main funtion of program
	open_browser()
	
	

	
