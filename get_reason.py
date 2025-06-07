from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from config import ATF_URL, USERNAME_, PASSWORD

driver = webdriver.Chrome()
driver.get(ATF_URL)

WebDriverWait(driver, 30).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "contents"))
)

username = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "login")))
username.send_keys(USERNAME_)

password = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "edtDsSenha")))
password.send_keys(PASSWORD)

login_button = driver.find_element(By.NAME, "btnAvancar")
login_button.click()

time.sleep(30)
driver.quit()