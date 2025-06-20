import json
from groq import Groq
import httpx

from config import API_KEY
from config import PROCESS_ATF_PATH, JSON_EMENTA_PATH



client = Groq(api_key=API_KEY, http_client=httpx.Client(verify=False))

with open("processos_ementa.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

try:
    with open("aa.json", "r", encoding="utf-8") as f_out:
        save_data = json.load(f_out)
        atfs_with_reason = {item["atf"] for item in save_data if "reason" in item and item["reason"].strip()}
except FileNotFoundError:
    atfs_with_reason = set()

for obj in dados:
    atf = obj.get("atf")
    content = obj.get("content")

    if atf in atfs_with_reason:
        continue
    
    if not obj:
        print("Erro: Objeto vazio.")
    elif not content:
        obj["reason"] = "Processo inexistente."
    else:
        content = obj.get("content", "")

        if not content.strip():
            print("Conteúdo vazio no primeiro objeto.")
            reason = "Processo inexistente."
        else:
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a senior tax auditor at the Paraíba State Department of Finance, and your mission is to analyze the reason why a process was denied."
                    },
                    {
                        "role": "user",
                        "content": f"You must read this text process limited by [] and extract the reason because this process was denied in portuguese. respond in  summary protuguese. The format is 'Reason: write here' .Text: [{content}]",
                    }
                ],
                temperature=0.5,
                max_completion_tokens=1024,
                top_p=0.65,
                stream=True,
                stop=None,
            )
    
            reason = ""
            for chunk in completion:
                part = chunk.choices[0].delta.content or ""
                reason += part 
        
            obj["reason"] = reason.strip()
    
    with open("aa.json", "w", encoding="utf-8") as f_out:
        json.dump(dados, f_out, ensure_ascii=False, indent=4)