
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
time.sleep(1)

driver.get('https://github.com/Vidoosh/Image-colorizer')
time.sleep(2)


try:
    repository_link = driver.find_element(By.LINK_TEXT, 'Image-colorizer')
    print("Repository exist.Downloading the file is possible")
except:
    print("Repository doesn't exist.Can't download the file")
finally:
    driver.quit()


   