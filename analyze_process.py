from groq import Groq

from config import API_KEY

client = Groq(api_key=API_KEY)
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are a senior tax auditor at the Paraíba State Department of Finance, and your mission is to analyze the reason why a process was denied."
        },
        {
            "role": "user",
            "content": ""
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")