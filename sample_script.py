from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# init driver
driver = webdriver.Chrome()
driver.maximize_window()

#it will be applied to wait.until
#it will check every 500ml
driver.wait = WebDriverWait(driver, timeout=10)

#always applied to all find element comands
# checks for element every 100ml sec
# the only way to set it off is by set it 0
#driver.implicitly_wait(0)
driver.implicitly_wait(5)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
#sleep(4)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
#driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK0000')), message='not clickble')
# click search

driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
