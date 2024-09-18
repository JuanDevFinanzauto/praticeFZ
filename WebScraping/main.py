import requests
from bs4 import BeautifulSoup

url = "https://www.finanzauto.com.co/portal/politicas"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    content = soup.find_all("span", {"class": "text-primary text-2x1 font font-bold"}) + soup.find_all("p", {"class": "text-justify"})

    with open("politicas.txt", "w", encoding="utf-8") as file:
        for element in content:
            file.write(element.get_text() + "\n")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
