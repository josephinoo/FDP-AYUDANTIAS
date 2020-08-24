def cargarDatos(nomFile):
    fichero=open(nomFile+".txt")
    diccionario=dict()
    for linea in fichero:
        ciudad,metrica,valor=linea.strip().split(",")
        metricas =diccionario.setdefault(ciudad,dict())
        metricas[metrica]=float(valor)
    fichero.close()
    return diccionario

datos=cargarDatos("datos")
print(datos)
paises={
    "Ecuador":["Guayaquil","Cuenca"],
    "Colombia":["Bogota"]
}

def metricaPais(datos,paises):
    diccionario=dict()
    for pais,ciudades in paises.items():
        precios=[]
        temperatura=[]
        for ciudad in ciudades:
            metricas=datos[ciudad]
            precios.append(metricas["precioCasas"])
            temperatura.append(metricas["temperatura"])
        diccionario[pais]={
            "precioCasas":sum(precios)/len(precios),
            "temperatura":sum(temperatura)/len(temperatura)
        }
    return diccionario

def generarPaises(promedios,metrica,minimo,maximo):
    fichero=open(metrica+".csv","w")
    for pais,metricas in promedios.items():
        valor=metricas[metrica]
        if minimo<valor<maximo:
            fichero.write(pais+","+metrica+","+str(valor)+"\n")
    fichero.close()

promedios=metricaPais(datos,paises)
print(promedios)
generarPaises(promedios,"precioCasas",120000,126000)

# d={"a":1,"b":2}

# a=d.setdefault("a",4)
# print(d)
# print(a)
