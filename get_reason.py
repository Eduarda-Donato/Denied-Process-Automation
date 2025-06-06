from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from config import PATH, EPROCESSO_URL, ATF_URL, USERNAME,PASSWORD
from get_indeferidos import get_indeferidos

processes = get_indeferidos(PATH)

driver = webdriver.Chrome()
driver.get(EPROCESSO_URL)

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys(USERNAME)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(PASSWORD)

login_button = driver.find_element(By.NAME, "submit")
login_button.click()

time.sleep(10)

menu_button = driver.find_element(By.ID, "menu-atf")
menu_button.click()

time.sleep(10)

consultar_button = driver.find_element(By.ID, "58519")
consultar_button.click()

time.sleep(15)

for process in processes:

    try:
        protocolo_field = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="numeroProtocolo"]')
        protocolo_field.clear()
        protocolo_field.send_keys(process)
        
        consultar_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-danger")
        consultar_button.click()
        
        time.sleep(15)
        
        protocolo_atf = driver.find_elements(By.XPATH, '//span[@class="responsive-title"]')[2]
        protocolo_atf.text
        print(protocolo_atf)
        
    except Exception as e:
        print(f"Erro no processo {process}: {e}")
        continue
driver.quit()


