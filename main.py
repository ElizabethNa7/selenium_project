from selenium import webdriver # webdriver is an automation tool that controls Google Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # used to search for elements within the HTML
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


service = Service(executable_path="/Users/elizabeth-na/selenium_project/chromedriver")
driver = webdriver.Chrome(service=service)


# driver.get("https://google.com")

# # just in case, wait for the search bar to exist on the page
# WebDriverWait(driver, 5).until( # 5 second timeout
#     EC.presence_of_element_located((By.NAME, 'q'))
# )

# # use google search bar to search something
# input_element = driver.find_element(By.NAME,"q")  # (By.CLASS_NAME,"gLFyf")better to use NAME than CLASS_NAME because classes change often ig
# input_element.clear() # used to just clear the element (the search bar in this case) in case it has anything in it already
# input_element.send_keys("Gojou Satoru" + Keys.ENTER)

# # navigate links based on text
# WebDriverWait(driver, 5).until( # 5 second timeout
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'jujutsu-kaisen'))
# )
# # link = driver.find_element(By.PARTIAL_LINK_TEXT, 'jujutsu-kaisen') # can use driver.find_elements() to get an array of links that contain that text
# link = driver.find_element(By.PARTIAL_LINK_TEXT, 'jujutsu-kaisen')
# link.click()
# # expansion idea: search character and use AI/data models to analyze and choose the "best" looking pic?

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"

WebDriverWait(driver, 5).until( # 5 second timeout
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")) # can find the XPATH by telling GPT the HTML element you want
)

# huh
# language = driver.find(By.XPATH, "//*[contains(text(), 'English')]"))

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()



time.sleep(10) # 10 seconds

driver.quit()