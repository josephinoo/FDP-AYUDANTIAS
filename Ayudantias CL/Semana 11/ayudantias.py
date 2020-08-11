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


m=cargarArchivo("archivo.txt")

print(m.size)
print(np.count_nonzero(m))
print(np.where("Anillo"==m)[0])
#print(ocurrencias("Sauron",cargarArchivo("archivo.txt")))
