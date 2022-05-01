import requests
from .config import settings
from bs4 import BeautifulSoup

URL = "https://programacao.portoitajai.com.br/"
page = requests.get(URL)

def main():
    print("Hello from Lucas", settings.NAME)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", class_="tab-content")
    tr_elements = results.find_all('table')

    for i in tr_elements:
        i_elements = i.find_all("tbody")
        for tr in i_elements:
            print(tr.find_all("td"))


    