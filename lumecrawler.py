import os
import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

def main():
    url: str = 'https://www.lume.ufrgs.br/discover'
    page: int = 1

    params = {
        'rpp': 100,
        'query': 'https://www.lume.ufrgs.br/discover',
        'page': f'{page}',
        'scope': '10183%2F1'
    }

    response = req.get(url, params=params)
    soup = bs(response.text, 'html.parser')
    
    # get div from id aspect_discovery_SimpleSearch_div_search-results
    lista_artigos = soup.find('div', id='aspect_discovery_SimpleSearch_div_search-results')
    
    
    
    print(soup.prettify())
    pass

if __name__ == '__main__':
    main()