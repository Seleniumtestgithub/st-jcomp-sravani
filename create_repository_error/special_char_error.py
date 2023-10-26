import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from logindata import USERNAME,PASSWORD



driver = webdriver.Firefox()


driver.get('http://www.github.com')


new_repository = driver.find_element(By.ID, 'global-create-menu-button')
new_repository.click()
time.sleep(1)
new_repository2 = driver.find_element(By.LINK_TEXT, 'New repository')
new_repository2.click()
time.sleep(5)

    
repository_name = driver.find_element(By.ID, ':r2:')
repository_name_input = 'github-automation-p9999'
try:
    if any(char in repository_name_input for char in r'~!@#$%^&*()+=\[]{}|;:,.<>?'):
        raise ValueError("Special characters are not allowed in the repository name")
    repository_name.send_keys(repository_name_input)
    time.sleep(2)
except ValueError as e:
    print(f"Error: {str(e)}")
    driver.quit()


repository_description = driver.find_element(By.ID, ':r3:')
repository_description.send_keys('GitHub Automation Using Selenium Part')
time.sleep(2)

repository_auto_init = driver.find_element(By.ID, ':r8:')
repository_auto_init.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

create_repo_button = driver.find_element(By.XPATH, '//button[@class="types__StyledButton-sc-ws60qy-0 iqZIXT"]')
create_repo_button.click()
time.sleep(5)

print("Here 3---created repo")


