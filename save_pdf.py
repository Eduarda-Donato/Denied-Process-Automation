import requests


def save_pdf(pdf_url, atf_number):
    response = requests.get(pdf_url)
    with open(f"pdf\\{atf_number}.pdf", "wb") as f:
        f.write(response.content)