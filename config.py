import os
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

INDEFERIDOS_PATH = "S:\\GET\\Geral\\PROCESSOS MENSAIS GET\\2025\\"
INDEFERIDOS_MES = "MAIO\\GET_ANÁLISE_22_24_V05_2025 05 31 maio.xlsx"
PATH = os.path.join(INDEFERIDOS_PATH, INDEFERIDOS_MES)

EPROCESSO_URL = "https://www5.sefaz.pb.gov.br/efisco/login?sistemaId=PROTE&buildVersion=2.0.0-SNAPSHOT&buildTimestamp=16/05/2025%2006:01&service=https://www5.sefaz.pb.gov.br/protocolo-eletronico%2Fj_spring_cas_security_check"
ATF_URL = "https://ap1pro.sefaz.pb.gov.br/atf/"