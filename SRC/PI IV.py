import cherrypy
import os.path
import os
import sys
import urllib.request
import bs4

class twopage(object):
    def index(self):
        return "página2"
    index.exposed = True

class onepage(object):
    threepage = twopage()
    #index.exposed=True
    def default(self,year,month,day):
        return "Data:"+year+"/"+month+"/"+day
    default.exposed=True

class helloworld:
    onepage = onepage()
    twopage = twopage()
    
    def index(self):
        return """<html>
                      <head>
                        <title>Kaizoku - Web Crawler</title>
                      </head>
                      <body>
                        <div style="width:300px; height:290px; margin: 10px auto 0px auto;">
                        <img style="width: 300px;height: 210px;" src="crawler/kaizoku5.png">
                      </div>
                      <div style="width:70%; height:80px; margin: 0 auto 60px auto; text-align:center;">
                        <form action ="dologin" method="POST" name="TstButton">
                            <div>Digite a URL desejada:</div>
                            <div>www.<input type=text style="width: 60%;height:30px;" size=70 maxlength=500 name="username" value=""></div>
                            <input type="radio" name="name" value="link" checked> Links <input type="radio" name="name" value="imagem"> Imagens<br>
                            <p><input type="submit" value="Pesquisar"/></p>
                        </form>
                      </div>
                      <div style="width:200px; height:290px; margin: 10px auto 25px auto;">
                        <img style="width: 202px;height: 156px;" src="crawler/navio_pirata.gif">
                      </div>
                      <style type="text/css">
                      body{
                       background:
                       url("crawler/sand.png") bottom repeat-x ;
                      }
                      </style>
                      </body>
                 </html>"""
    index.exposed = True



    def foo(self):
        return "foo"
    foo.exposed = True

    def dologin(self,username,name):
        codigo1 = """<html>
                        <head>
                            <title>Kaizoku - Web Crawler</title>
                                <style type="text/css">
                                    body{
                                        background:
                                        url("crawler/sand.png") bottom repeat-x ;
       
                                    }
                                </style>
                         </head>
                         <body>
                             <div style="width:100%; height:140px; margin: 0px;text-align:center">
                                 <a href = http://localhost:8080><img style="width: 159px;height: 140px;" align="left" src="crawler/mapa_voltar3.png"></a>
                                 <img style="width: 279px;height: 58px;margin: 38px 223px 25px auto" align="center" src="crawler/kaizoku_name.png">
                                 <h2 align = "center">Resultado para """ + name + """ da Url:<br>
                                 <center><font color = "red">"""+username+"""</font>
                             </div>
                             <div style="width:70%; margin: 85px auto 180px auto;text-align:center;">"""
        codigo3 = """</div>
                     </body>
                     </html>"""
        def codigo (http, url):
            codigo = urllib.request.urlopen(http + url)
            documento = codigo.read()
            lista = bs4.BeautifulSoup(documento)
            return lista

        def pegalink (lista,url):
            codigo1 = """<tr>
                         <td>
                         <a href="""
            codigo2 = """>"""
            codigo3 = """</a>
                         </td>
                         </tr>
                         <br>"""
            codigo5 = ""

            for link in lista.findAll('a'):
                if link.get('href'):
                    y = link.get('href')
                    if y.find(url) != -1:
                        codigo5 = codigo5 + codigo1 + y + codigo2 + y + codigo3
                    else:
                        if y.find("http") == -1:
                            if y[:1] == "/":
                                codigo5 = codigo5 + codigo1 + (url + y) + codigo2 + (url + y) + codigo3
                            else:
                                codigo5 = codigo5 + codigo1 + (url + "/" + y) + codigo2 + (url + "/" + y) + codigo3
            return codigo5

        def downloadimg (lista, url):
            n = 0
            imagem = """<img src="crawler/imagem/"""
            imagem1 = """" width="150" height="130"/>"""
            imagem2 = ""
            for x in lista.findAll('img'):
                n = n + 1
                if x.get('src'):
                        img = x.get('src')
                        if img.find(url) != -1:
                                img = img
                        else:
                                if img.find("http") == -1:
                                        if img[:1] == "/":
                                                img = ("http://www." + url + img)
                                        
                                        else:
                                                img = ("http://www." + url + "/" + img)
                                                
                        
                        webFile = urllib.request.urlopen(img)
                        extensao = ''
                        for x in range(len(img)):
                                extensao = img[len(img) - 1 - x] + extensao
                                x= x - 1
                                if extensao[0] == '.':
                                        break
                                
                        if extensao == '.gif':
                                localFile = open("C:/Users/pc/Desktop/PI IV/Crawler/Imagem/" + str(n) +".gif", 'wb')
                                imagem2 = (imagem2 + imagem + str(n) + ".gif" + imagem1)
                        else:
                                localFile = open("C:/Users/pc/Desktop/PI IV/Crawler/Imagem/" + str(n) +".jpg", 'wb')
                                imagem2 = (imagem2 + imagem + str(n) + ".jpg" + imagem1)
                        localFile.write(webFile.read())
                        webFile.close()
                        localFile.close()
            return imagem2
        
        http = ("http://www.")
        lista = codigo(http,username)
        if (name == "link"):
            codigo2 = pegalink(lista,username)
        if (name == "imagem"):
            img =(len(lista.findAll('img')))
            codigo2 = downloadimg(lista, username)
        return (codigo1 + codigo2 + codigo3)
    dologin.exposed = True

    def default(self,qqcoisa):
        return "Não tem esse caminho."
    default.exposed=True

tutconf = os.path.join('.', 'tutorial.conf')
cherrypy.quickstart(helloworld(), config=tutconf)