import json
from groq import Groq
import httpx

from config import API_KEY, JSON_EMENTA_PATH

# Caminho do JSON que tem o conteúdo HTML de um processo

client = Groq(api_key=API_KEY, http_client=httpx.Client(verify=False))

# Lê o JSON que contém o conteúdo HTML
with open(JSON_EMENTA_PATH, "r", encoding="utf-8") as f:
    dados = json.load(f)
    
obj = dados[1] if dados else None

if not obj:
    print("Lista vazia no JSON.")
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
                    "content": f"You must read this text process limited by [] and extract the reason because this process was denied in portuguese. respond in protuguese. Text: [{content}]",
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

    reason = reason.strip()
    obj["justificativa"] = reason or "Processo inexistente."

    # Salva só o primeiro objeto atualizado em um novo arquivo
    with open("processo_primeiro_resultado.json", "w", encoding="utf-8") as f_out:
        json.dump(obj, f_out, ensure_ascii=False, indent=4)

    print("Processamento do primeiro processo concluído.")