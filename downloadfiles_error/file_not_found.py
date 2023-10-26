from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
time.sleep(1)

driver.get('https://github.com/Vidoosh/Image-colorizer')
time.sleep(2)

try:
    code = driver.find_element(By.CSS_SELECTOR, '#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > span.d-none.d-md-flex.ml-2 > get-repo > feature-callout')
    code.click()
    time.sleep(1)
    download = driver.find_element(By.CSS_SELECTOR, '#local-panel > ul > li:nth-child(3) > a')
    download.click()
except NoSuchElementException:
    print("File is not available for download")
finally:
    driver.quit()
