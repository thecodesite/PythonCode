
# Opening and Closing using selenium
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
