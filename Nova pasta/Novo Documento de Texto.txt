import urllib.request
#import sys
#import re
import bs4

def codigo (http, url):
        codigo = urllib.request.urlopen(http + url)
        documento = codigo.read()
        lista = bs4.BeautifulSoup(documento)
        return lista

def pegalink (lista, url):
        for link in lista.findAll('a'):
                if link.get('href'):
                        y = link.get('href')
                        if y.find(url) != -1:
                                print (y)
                        else:
                                if y.find("http") == -1:
                                        if y[:0] == "/":
                                                print (url + y)
                                        else:
                                                print(url + "/" + y)

def achaimg (lista):
        listaimg = []
        for link in lista.findAll('img'):
                if link.get('src'):
                        listaimg.append(link.get('src')
        return listaimg

def downloadimg (listaimg, img):
        for x in img: 
                webFile = urllib.request.urlopen()
                localFile = open("c:/users/pc/desktop/pi iv/Imagem/" + x +".jpg", 'wb')
                localFile.write(webFile.read())
                webFile.close()
                localFile.close()

        
http = ("http://www.")
url = input("Digite o site da pesquisa: www.")
#lista = codigo(http , url)
#pegalink(lista, url)
listaimg = achaimg(lista)
img =(len(lista.findAll('img')))
downloadimg(listaimg, img)
