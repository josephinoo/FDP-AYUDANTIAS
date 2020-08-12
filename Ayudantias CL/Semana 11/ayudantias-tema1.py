import numpy as np
def cargarArchivo(nombre):
    archivo=open(nombre,encoding="utf-8")
    lineas=archivo.readlines()
    matriz=np.zeros((len(lineas),30),dtype="<U20")
    for fila,linea in enumerate(lineas):
        linea_sep=linea.strip().split(" ")
        for columna,palabra in enumerate(linea_sep):
            matriz[fila,columna]=palabra
    return matriz

def ocurrencias(palabra,M):
    return len(M[np.where(palabra==M)])

def lineas(palabra,M):
    return tuple(np.where(palabra==m)[0])

def contarPalabras(M,stopwords):
    total_palas=np.count_nonzero(M)
    cant_stop=0
    for i in stopwords:
        if i in M:
            cant_stop+=1
    return(total_palas,cant_stop)

def concordancia(M,stopwords):
    diccionario=dict()
    total_palas,total_stopwords=contarPalabras(M,stopwords)
    diccionario["NTP"]=total_palas
    diccionario["NPC"]=total_stopwords
    conjuntoPalas=set()
    for i in range(len(M)):
        conjuntoPalas.update(set(M[i]))
    conjuntoPalas=conjuntoPalas.difference(set(stopwords))
    dic_palas=dict()
    for i in conjuntoPalas:
        dic_pala=dict()
        veces=ocurrencias(i,M)
        NL=lineas(i,M)
        dic_pala["veces"]=veces
        dic_pala["NL"]=NL

        dic_palas[i]=dic_pala
    
    diccionario["palabras"]=dic_palas
    return diccionario

m=cargarArchivo("archivo.txt")
stopwords=["la","con"]
print(concordancia(m,stopwords))

