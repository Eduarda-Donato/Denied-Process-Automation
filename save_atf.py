import json

from config import PATH, USERNAME_, PASSWORD
from get_atf import get_atf


processes = get_atf(PATH, USERNAME_, PASSWORD)

with open("processos_atf.json", "w", encoding="utf-8") as f:
    json.dump(processes, f, ensure_ascii=False, indent=4)


