import os
import json
from bs4 import BeautifulSoup

from config import HTML_PATH, PROCESS_ATF_PATH, JSON_EMENTA_PATH


with open(PROCESS_ATF_PATH, 'r', encoding='utf-8') as f:
    dados = json.load(f)
    
selector = "p.MsoNormal, p.MsoBodyTextIndent2, p.MsoBlockText, p.MsoBodyText, .Default b, h1, h2, p"


for obj in dados:
    atf = obj.get("atf")
    if not atf:
        obj["ementa"] = ""
        obj["content"] = ""
        continue

    ementa = ""
    content_process = ""

    fname = f"{atf}.html"
    html_path = os.path.join(HTML_PATH, fname)

    if os.path.exists(html_path):
        with open(html_path, "r", encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")

        elements_p = soup.find_all("p")
        elements = soup.select(selector)
        
        content_process = "\n\n".join([p.get_text(strip=True) for p in elements_p])
        
        for el in elements:
            text = el.get_text().strip()
            if "INDEFERIMENTO" in text or "PEDIDO DENEGADO" in text:
                ementa = text
                break
        
    obj["content"] = content_process   
    obj['ementa'] = ementa
    
with open(JSON_EMENTA_PATH, 'w', encoding='utf-8') as f_out:
    json.dump(dados, f_out, ensure_ascii=False, indent=4)
    