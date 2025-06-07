from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from config import EPROCESSO_URL
from get_denied import get_denied



def get_atf(path, username_,  password):
    eprocesso = get_denied(path)
    processes = []

    driver = webdriver.Chrome()
    driver.get(EPROCESSO_URL)

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username_)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()

    time.sleep(7)

    menu_button = driver.find_element(By.ID, "menu-atf")
    menu_button.click()

    time.sleep(7)

    consultar_button = driver.find_element(By.ID, "58519")
    consultar_button.click()

    time.sleep(10)

    for process in eprocesso:

        try:
            protocolo_field = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="numeroProtocolo"]')
            protocolo_field.clear()
            protocolo_field.send_keys(process)
            
            consultar_button = driver.find_element(By.XPATH,"//button[@type='button' and contains(@class, 'btn-danger') and contains(normalize-space(), 'Consultar')]")
            consultar_button.click()
            
            time.sleep(5)
            
            protocolo_atf = WebDriverWait(driver, 720).until(EC.presence_of_element_located((By.XPATH, "//td[span[contains(text(), 'Protocolo no ATF:')]]")))
            protocolo_atf = protocolo_atf.text
            protocolo_atf = protocolo_atf.replace("Protocolo no ATF:", "").strip()

            processes.append({
                "eprocesso": process,
                "atf": protocolo_atf
            })
            
        except Exception as e:
            print(f"Erro no processo {process}: {e}")
            processes.append({
                "eprocesso": process,
                "atf": "erro"
            })
            continue


    driver.quit()

    return processes


