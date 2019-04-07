import re

def reglas(archivotxt):
    mitxt= open(archivotxt, "r")
    lineas = mitxt.read()
    linea= lineas.splitlines()
    x=0
    lista=[]
    lista2=[]
    contadorLista=0
    a=""
    b=""
    
    while x<len(linea):
        if 1<=len(linea[x])<71 and linea[x][:1]!='-' and linea[x][-1:]!=':':
            y="<h1>" + linea[x] + "</h1>"
        
        elif linea[x][:1]=='-':
            elemento=linea[x][1:]
            lista.append(elemento)
            
            
            if len(lista)==1:
                y="<li>"+str(lista[contadorLista])+"</li>"
            elif len(lista)>1:
                y="<li>"+str(lista[contadorLista])+"</li>"
            contadorLista+=1
      
        else:
            y="<p>"+ linea[x] + "</p>"

                    
        #lista2.append(y)
        a=a+y
        x=x+1
    return a
    


'''def validarurl(url):  
    if re.search("^(http?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\?$", url):
        print ("url correcta")
    else:
        print ("url incorrecta")
        
        
url="www.as.com"
cadenaregular="^(http?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\?$"

validarurl(url)
#archivotxt="Z:\practica\mitexto.txt"'''



    