import requests
from bs4 import BeautifulSoup

def buscaGupy(cidade):
    data = {}
    for link in links:
        if "candidates" in link or "zendesk" in link or "#" in link:
            continue
        else:
            result2 = requests.get(link)
            soup2 = BeautifulSoup(result2.content, 'html.parser')
            soup3 = BeautifulSoup(soup2.prettify(),"html.parser")
            links2 = soup3.find_all("tr", attrs={'data-workplace':str(cidade)})
            data2 = {}
            for link2 in links2:
                title2 = link2.string
                data2[title2] = link2.get_text()
                print(link + " - " + str(cidade))
    

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "site:gupy.io"

links = []
  
for j in search(query, tld="com.br", num=100, stop=None, pause=2): 
    links.append(j)

buscaGupy("Curitiba")
buscaGupy("São José dos Campos")
buscaGupy("Jacareí")
buscaGupy("Colombo")
buscaGupy("São José dos Pinhais")
buscaGupy("Pinhais")

