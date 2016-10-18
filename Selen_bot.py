import time
from selenium import webdriver
import sys
import base64

#Obfuscate Information
log_name = base64.b64encode('')
pswd = base64.b64.encode('')


# Path to Chromedriver binary file
Chromedriver = 'C:\Users\Deaunna\Documents\chromedriver_win32\chromedriver' 


try:
	# Instantiate webdriver class into object
	driver = webdriver.Chrome(Chromedriver)
#Fetch url via HTTP protocol
	driver.get('https://calbike.nationbuilder.com/admin/signups/dedupe')
except:
	print 'Something is wrong with Chromedriver'
	sys.exit

#Select button for reviewing potential matches
	driver.get_element_by_class_name('button btn-primary').click()

#Return the the number of potential matches for review
	driver.get_element_by_class_name('stat')
	return duplicates

#Stop the browser
	time.sleep(6)

#Select the name from Nationbuilder Database
	signup_name = driver.find_element_by_class_name('sign-up')

#Stop browser again
	time.sleep(5)

# Quit selenium
	driver.quit()
