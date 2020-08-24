def cuentaEtiquetas(tendencias,listaFechas):
    diccionario=dict()
    for fecha in listaFechas:
        hashtags=tendencias[fecha]
        for tag in hashtags:
            diccionario.setdefault(tag,0)
            diccionario[tag]+=1
    return diccionario
tendencias = {
    '08-22-2016': {'#Rio2016', '#BSC', '#ECU'},
    '08-25-2016': {'#GYE', '#BRA','#BSC'}, 
    '08-27-2016': {'#YoSoyEspol', '#GYE', '#BSC'}
    }
listaFechas=['08-22-2016', '08-25-2016', '08-27-2016']

def reportaTendencias(tendencias,listaFechas):
    diccionario=cuentaEtiquetas(tendencias,listaFechas)
    veces=len(listaFechas)
    print("Literal a")
    for tag,cantidad in diccionario.items():
        if cantidad==veces:
            print("El tag "+tag+" esta presente en todas las fechas")
        
    print("Literal b")
    tags=list(diccionario.keys())
    print("Los tags ",tags," estan presente en al menos una de las fechas")

def tendenciasExcluyentes(tendencias,fecha1,fecha2):
    set_f1=tendencias[fecha1]
    set_f2=tendencias[fecha2]
    return set_f1.symmetric_difference(set_f2)

print(tendenciasExcluyentes(tendencias,'08-22-2016','08-27-2016'))
#reportaTendencias(tendencias,listaFechas)
print(cuentaEtiquetas(tendencias,listaFechas))
