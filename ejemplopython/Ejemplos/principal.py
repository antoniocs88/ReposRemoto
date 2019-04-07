from Ejemplos.reglas import *


def convertirTexto(archivotxt, archivohtml):

    f = open(archivohtml, "w")
    f.write("<html><body>")

    
    f.write(reglas(archivotxt))
    f.write("</body></html>")
    f.close()
    
    
archivotxt="Z:\practica\mitexto.txt"
archivohtml="Z:\practica\mihtml.html"

convertirTexto(archivotxt, archivohtml)
print(reglas(archivotxt))

                
