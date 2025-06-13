import os
import json
from bs4 import BeautifulSoup

from config import HTML_PATH, PROCESS_ATF_PATH, JSON_EMENTA_PATH


with open(PROCESS_ATF_PATH, 'r', encoding='utf-8') as f:
    dados = json.load(f)

files = os.listdir(HTML_PATH)

for obj in dados:
    atf = obj.get("atf")
    ementa = ""

    if not atf:
        obj["ementa"] = ""
        continue


    for file in files:
        if file.endswith('.html'):
            html_path = os.path.join(HTML_PATH, file)
            
            with open(html_path, 'r', encoding='utf-8') as f:
                html = f.read()
                
            soup = BeautifulSoup(html, "html.parser")
            
            for p in soup.select("p.MsoNormal"):
                p_text = p.get_text()
                if "INDEFERIMENTO" in p_text:
                    ementa = p_text.strip()
                    break
            
            if ementa:
                break
            
    obj['ementa'] = ementa
    
with open(JSON_EMENTA_PATH, 'w', encoding='utf-8') as f_out:
    json.dump(dados, f_out, ensure_ascii=False, indent=4)
    