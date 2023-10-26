

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time



driver = webdriver.Firefox()

driver.get('https://github.com/Vidoosh/Image-colorizer')
time.sleep(2)


code = driver.find_element(By.CSS_SELECTOR, '#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > span.d-none.d-md-flex.ml-2 > get-repo > feature-callout')
code.click()
time.sleep(1)
try:
    download = driver.find_element(By.CSS_SELECTOR, '#local-panel > ul > li:nth-child(3) > a')
    download.click()
    print("Download initiated successfully")

except NoSuchElementException as e:
    print("Download button not found")

finally:
    driver.quit()

