import os
import sys
import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

def download_pdf(url: str, link: str, folder: str):
    # Check if the folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = req.get(link)
    soup = bs(response.text, 'html.parser')
    div = soup.find('div', class_='item-page-field-wrapper table word-break')
    link_pdf = url + div.find('a')['href']
    # download the pdf file
    response = req.get(link_pdf)
    # save the pdf file
    with open(f'{folder}/{link_pdf.split("?")[-2].split("/")[-1]}', 'wb') as f:
        f.write(response.content)
        
def main(folder: str = 'files'):
    url: str = 'https://www.lume.ufrgs.br'
    page: int = 1

    params = {
        'rpp': 100,
        'query': 'sensoriamento+remoto+carbono+vegetacao',
        'page': f'{page}',
        'scope': '10183%2F1'
    }
    #url_final = url + '/discover'
    url_final = 'https://www.lume.ufrgs.br/handle/10183/40514/discover?query=sensoriamento+remoto+carbono+vegeta%C3%A7%C3%A3o&rpp=100&sort_by=score&order=desc&dateMode=select&querytype_0=title&query_relational_operator_0=contains&query_value_0=&querytype_1=author&query_relational_operator_1=contains&query_value_1=&querytype_2=subject&query_relational_operator_2=contains&query_value_2=&querytype_3=tipo&query_relational_operator_3=equals&query_value_3=&querytype_4=dateIssued&query_relational_operator_4=contains&query_value_4=&select_mes_inicio_4=&select_dia_inicio_4=&select_mes_fim_4=&select_dia_fim_4=&querytype_5=dataAno&query_relational_operator_5=equals&query_value_5=&querytype_6=idioma&query_relational_operator_6=equals&query_value_6=&querytype_7=formatoArquivo&query_relational_operator_7=equals&query_value_7=&querytype_8=serie&query_relational_operator_8=contains&query_value_8=&querytype_9=authortd&query_relational_operator_9=contains&query_value_9=&querytype_10=orientador&query_relational_operator_10=contains&query_value_10=&querytype_11=acervo&query_relational_operator_11=contains&query_value_11=&querytype_12=descriptionSection&query_relational_operator_12=contains&query_value_12=&querytype_13=tipoAto&query_relational_operator_13=contains&query_value_13=&querytype_14=natureza&query_relational_operator_14=contains&query_value_14=&querytype_15=numeroAto&query_relational_operator_15=contains&query_value_15=&querytype_16=orgao&query_relational_operator_16=contains&query_value_16=&querytype_17=dataFinal&query_relational_operator_17=contains&query_value_17=&select_mes_inicio_17=&select_dia_inicio_17=&select_mes_fim_17=&select_dia_fim_17=&querytype_18=programa&query_relational_operator_18=contains&query_value_18=&querytype_19=entrevistado&query_relational_operator_19=contains&query_value_19=&querytype_20=grandeArea&query_relational_operator_20=contains&query_value_20=&querytype_21=tipoDeApresentacao&query_relational_operator_21=contains&query_value_21=&querytype_22=areaTematica&query_relational_operator_22=contains&query_value_22=&querytype_23=coordenador&query_relational_operator_23=contains&query_value_23=&querytype_24=origem&query_relational_operator_24=contains&query_value_24=&querytype_25=unidade&query_relational_operator_25=contains&query_value_25=&querytype_26=status&query_relational_operator_26=contains&query_value_26=&querytype_27=curso&query_relational_operator_27=contains&query_value_27=&querytype_28=nivelAcademico&query_relational_operator_28=contains&query_value_28=&querytype_29=nivelDeEnsino&query_relational_operator_29=contains&query_value_29=&querytype_30=tipoDeMaterial&query_relational_operator_30=contains&query_value_30=&submit-search='
    params = {}
    response = req.get(url_final, params=params)
    soup = bs(response.text, 'html.parser')

    list_results = soup.find('div', id='aspect_discovery_SimpleSearch_div_search-results')
    lista_links = []
    resultado_lista = list_results.find_all('div', class_='col-sm-9 artifact-description')
    for resultado in resultado_lista:
        lista_links.append(resultado.find('a')['href'])
    for link in lista_links:
        download_pdf(url, link, folder)



if __name__ == '__main__':
    folder = sys.argv[1]
    main(folder=folder)