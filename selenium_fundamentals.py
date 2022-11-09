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
