from bs4 import BeautifulSoup
from datetime import date
import requests
import time

def noticiasdodia():
    hoje = str(date.today())
    codigohtml = requests.get('https://noticias.uol.com.br').text
    soup = BeautifulSoup(codigohtml,'lxml')
    noticias = soup.find_all('div', class_='thumbnails-wrapper')
    for index , noticia in enumerate(noticias):
        titulo_noticia = noticia.find('h3').text
        link_noticia = noticia.a['href']
        with open(f'noticias/{index}.txt' , 'w') as f:
            f.write(f"Titulo da Noticia: {titulo_noticia}\n")
            f.write(f"Data de acesso: {hoje}\n")
            f.write(f"Link da noticia: {link_noticia}\n")
            print(f'Arquivo salvo com sucesso! {index}.txt')

if __name__ == '__main__':
    while True:
        noticiasdodia()
        tempominutos=10
        print(f'Esperando {tempominutos} minutos...')
        time.sleep(tempominutos * 60)





