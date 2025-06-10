#entrar na pasta de pdf de acodor dom o atf fazer pesquisa com o groq, add resultado no json

import fitz 

def extrair_texto_pdf(caminho_arquivo):
    texto = ""
    pdf = fitz.open(caminho_arquivo)
    for pagina in pdf:
        texto += pagina.get_text() + "\n"
    return texto


caminho = "seu_arquivo.pdf"
print(extrair_texto_pdf(caminho))
