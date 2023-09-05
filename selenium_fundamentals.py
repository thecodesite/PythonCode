##Common libraries and packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# To avoid ElementClickInterceptedException: Message: element click intercepted
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##To click() on the clickable element you need to induce WebDriverWait
##for the element_to_be_clickable() and you can use either of the
##following locator strategies:

#Using CSS_SELECTOR:
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "element"))).click()

#Using XPATH:
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "element"))).click()

#Using XPATH and inner text:
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='text']"))).click()

#Note: You have to add the following imports:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

## Opening and Closing using selenium

# Import module
from selenium import webdriver

# Create object
driver = webdriver.Chrome()

# Fetching the Url
url = "Webpage"

# New Url
new_url = "New webpage"

# Opening first url
driver.get(url)

# Open a new window
driver.execute_script("window.open('');")

# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)

# Closing new_url tab
driver.close()

# Switching to old tab
driver.switch_to.window(driver.window_handles[0])

##Get current url

print(driver.current_url)

## Print Webpage to PDF
import json
from selenium import webdriver
filename='FILENAME'
chrome_options = webdriver.ChromeOptions()
settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),'savefile.default_directory':downloadPath}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://google.com/")
browser.execute_script("document.title = \'{}\'".format(filename))
browser.execute_script('window.print();')
browser.close()


#Importing the libraries to get the webdriver
#pip install wget
import requests
import wget
import zipfile
import os

# get the latest chrome driver version number
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text

# build the donwload url
download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_mac64.zip"

# download the zip file using the url built above
latest_driver_zip = wget.download(download_url,'chromedriver.zip')

# extract the zip file
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall("../ChromeDriver_Path") # you can specify the destination folder path here
# delete the zip file downloaded above
os.remove(latest_driver_zip)
