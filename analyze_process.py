import json
from groq import Groq
import httpx

from config import API_KEY
from config import PROCESS_ATF_PATH, JSON_EMENTA_PATH



client = Groq(api_key=API_KEY, http_client=httpx.Client(verify=False))

with open("processos_ementa.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    
for obj in dados:
    atf = obj.get("atf")
    content = obj.get("content")
    
    if not content:
        obj["justificativa"] = "Processo inexistente."
        continue

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a senior tax auditor at the Paraíba State Department of Finance, and your mission is to analyze the reason why a process was denied. T"
            },
            {
                "role": "user",
                "content": f"You must read this text process limited by [] and extract the reason because this processe was denied in portuguese. The reason must be no more than 4 words, a exemplo of reason is 'Impedimento legal'. Text: [{content}]",
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
        
    obj["content"] = reason.strip()
    
with open("aa.json", "w", encoding="utf-8") as f_out:
    json.dump(dados, f_out, ensure_ascii=False, indent=4)