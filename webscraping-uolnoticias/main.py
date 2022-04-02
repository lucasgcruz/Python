from bs4 import BeautifulSoup
from datetime import date
import requests
import time

def noticiasdodia(): #função para coleta e registro de notícias
    hoje = str(date.today()) #acesso a data atual para registro posterior
    codigohtml = requests.get('https://noticias.uol.com.br').text #leitura do código html5 da página inicial da UOL
    soup = BeautifulSoup(codigohtml,'lxml') #transforma o codigo html em objetos
    noticias = soup.find_all('div', class_='thumbnails-wrapper') #captura todas as noticias de acordo com a classe da thumbnail
    for index , noticia in enumerate(noticias): #numera cada repetição na variavel index
        titulo_noticia = noticia.find('h3').text #captura o titulo da noticia
        link_noticia = noticia.a['href'] #captura o link da noticia
        with open(f'noticias/{index}.txt' , 'w') as f: #funcao para registro do arquivo
            f.write(f"Titulo da Noticia: {titulo_noticia}\n") #registro do titulo
            f.write(f"Data de acesso: {hoje}\n") #registro da data de acesso (dia atual)
            f.write(f"Link da noticia: {link_noticia}\n") #registro do link referente a noticia
            print(f'Arquivo salvo com sucesso! {index}.txt') #confirmacao de registro com numero do arquivo

if __name__ == '__main__': #repeticao da funcao a cada 10 minutos
    while True:
        noticiasdodia()
        tempominutos=10 #intervalo em minutos
        print(f'Esperando {tempominutos} minutos...') #mensagem inicio do intervalo
        time.sleep(tempominutos * 60) # intervalo em minutos convertido para segundos





