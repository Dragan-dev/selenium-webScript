import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/home/laki/Documents/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.helloworld.rs/kompanije")
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)


search = driver.find_element(By.ID, "search")
search.send_keys("Mera")
search.send_keys(Keys.RETURN)
time.sleep(5)

try:
    chased_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "45 iskustava")))
    chased_link.click()
    cookies_click = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "U redu")))
    cookies_click.click()
except:
    driver.close()
