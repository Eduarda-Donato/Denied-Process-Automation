from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from config import ATF_URL, PROCESS_ATF_PATH, USERNAME_, PASSWORD
from read_atf import read_atf
from save_pdf import save_pdf


driver = webdriver.Chrome()
driver.get(ATF_URL)

WebDriverWait(driver, 30).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "contents"))
)

username = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "login")))
username.send_keys(USERNAME_)

password = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "edtDsSenha"))
)
password.send_keys(PASSWORD)

login_button = driver.find_element(By.NAME, "btnAvancar")
login_button.click()


WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "menu"))
)

Legislacao_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Legislação"))
)
Legislacao_button.click()

tributacao_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Tributação"))
)
tributacao_button.click()

parecer_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Parecer"))
)
parecer_button.click()

consultar_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Consultar"))
)
consultar_button.click()

driver.switch_to.default_content()

WebDriverWait(driver, 30).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "contents"))
)

WebDriverWait(driver, 30).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "principal"))
)

radio_button = WebDriverWait(driver, 3000).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='rdbCriterio' and @value='nrProcesso']"))
)
radio_button.click()

atf_processes = read_atf(PROCESS_ATF_PATH)

erro_atf = []

for process in atf_processes:
        atf_process = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.NAME, "edtCriterio"))
        )
        atf_process.clear()         
        atf_process.send_keys(process)

        search_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.NAME, "btnPesquisar"))
        )
        search_button.click()
        
        original_window = driver.current_window_handle
        
        try:
                parecer_link = WebDriverWait(driver, 60).until(
                        EC.element_to_be_clickable((
                                By.XPATH,
                                "//a[contains(@onclick, 'aoClicarDetalharParecLink')]"
                        ))
                )
                #parecer_number = parecer_link.text.strip()
                parecer_link.click()
                
                WebDriverWait(driver, 60).until(lambda d: len(d.window_handles) == 2)
                
                new_window = [window for window in driver.window_handles if window != original_window][0]
                

                driver.switch_to.window(new_window)
                pdf_url = driver.current_url

                save_pdf(pdf_url, process)
                #save_pdf(pdf_url,parecer_number)

                driver.close()

                driver.switch_to.window(original_window)

                WebDriverWait(driver, 60).until(
                        EC.frame_to_be_available_and_switch_to_it((By.ID, "contents"))
                )
                
                WebDriverWait(driver, 60).until(
                        EC.frame_to_be_available_and_switch_to_it((By.ID, "principal"))
                )
        except Exception as e:
                erro_atf.append(process)
                print(f"Erro no processo {process}: {e}")
                
                WebDriverWait(driver, 60).until(
                        EC.frame_to_be_available_and_switch_to_it((By.ID, "contents"))
                )
                
                WebDriverWait(driver, 60).until(
                        EC.frame_to_be_available_and_switch_to_it((By.ID, "principal"))
                )
                continue

driver.quit()

print(erro_atf)