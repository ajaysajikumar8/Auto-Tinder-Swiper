import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

EMAIL = ""
PASSWORD = ""

chrome_driver_path = "E:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get(url="https://tinder.com")

time.sleep(5)

login = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(2)

try:
    login_using_fb = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')    
except NoSuchElementException:
    more_options_btn = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/button')
    more_options_btn.click()
    time.sleep(3)
    login_using_fb = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')    
finally:
    login_using_fb.click()
        
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

#switching to fb login window
driver.switch_to.window(fb_login_window)

#Authentication
email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(4)
#switching back to base window
driver.switch_to.window(base_window)

time.sleep(15)
location_enable = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]/span')
location_enable.click()

time.sleep(2)
notifications_dialog_disable = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[2]/span')
notifications_dialog_disable.click()

time.sleep(1)
cookie_enabler = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookie_enabler.click()

time.sleep(5)

for n in range(70):

    time.sleep(5)

    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()

    except ElementClickInterceptedException:

        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)
