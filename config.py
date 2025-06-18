import os
from dotenv import load_dotenv


load_dotenv()

USERNAME_ = os.getenv("USERNAME_")
PASSWORD = os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")

#DENIED_PATH = "S:\\GET\\Geral\\PROCESSOS MENSAIS GET\\2025\\"
#DENIED_MONTH = "MAIO\\GET_ANÁLISE_22_24_V05_2025 05 31 maio.xlsx"
#PATH = os.path.join(DENIED_PATH, DENIED_MONTH)
 
PATH = "C:\\Users\\eduar\\Documents\\indeferidos\\GET_ANÁLISE_22_24_V05_2025 05 31 maio.xlsx"
PROCESS_ATF_PATH = "processos_atf.json"
HTML_PATH = "C:\\Users\\maria.donato\\Documents\\Portfolio\\indeferidos\\html\\"

JSON_EMENTA_PATH = "processos_ementa.json"

EPROCESSO_URL = "https://www5.sefaz.pb.gov.br/efisco/login?sistemaId=PROTE&buildVersion=2.0.0-SNAPSHOT&buildTimestamp=16/05/2025%2006:01&service=https://www5.sefaz.pb.gov.br/protocolo-eletronico%2Fj_spring_cas_security_check"
ATF_URL = "https://www4.sefaz.pb.gov.br/atf/"
