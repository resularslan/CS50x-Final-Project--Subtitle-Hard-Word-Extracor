import requests
from bs4 import BeautifulSoup

# Clean definitions string from wiktionary
def cleanString(text):
    soup = BeautifulSoup(text, "html.parser")
    for span in soup.find_all("span"):
        span.decompose() 
    return soup.get_text().strip()

# Gets word, part of speech and definiton of word from wiktionary
def get_wiktionary_definition(word):
    url = f"https://en.wiktionary.org/api/rest_v1/page/definition/{word}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "en" in data:
            meanings = []
            for meaning in data["en"]:
                pos = meaning.get("partOfSpeech", "Unknown")
                definition = meaning["definitions"][0].get("definition", "No definition found")
                meanings.append((word.upper(), pos, cleanString(definition)))
            return meanings
    return [(word.upper(), "", "")]