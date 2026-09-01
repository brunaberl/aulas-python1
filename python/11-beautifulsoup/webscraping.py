#scrapng é buscar informacoes em um site e trazer para dentro do seu script
import requests

from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')

dados_pagina = BeautifulSoup(pagina.text, "html.parser")

#(print(dados_pagina.prettify()))

#todas_frases = dados_pagina.find_all('div', class_='quote')

#for div in todas_frases:
    #print(div)

todasFrasesFiltradas = dados_pagina.find_all('span', itemprop="text")

for span in todasFrasesFiltradas:
    print(span.text)
    