def calcularFecha(fecha,n):
    import datetime as dt
    dia_entregado=dt.datetime.strptime(fecha,'%d-%m-%Y')
    dia_resta=dia_entregado-dt.timedelta(days=n)
    fecha_str=dia_resta.strftime("%d-%m-%Y")
    return fecha_str

def cargarDatos(nomA):
    choferes=set()
    diccionario=dict()
    archivo=open(nomA+".txt")
    archivo.readline()
    for linea in archivo:
        id_ruta,id_chofer,fecha=linea.strip().split(",")
        choferes.add(id_chofer)
        dict_ruta=diccionario.setdefault(id_ruta,dict())
        conjunto_fecha=dict_ruta.setdefault(fecha,set())
        conjunto_fecha.add(id_chofer)
    archivo.close()
    return (choferes,diccionario)

def encontrarChoferes(dicc,fecha,losChoferes,id_ruta,n):
    dicc_fechas=dicc[id_ruta]
    choferes_fecha=set()
    for i in range(1,n+1):
        fecha_select=calcularFecha(fecha,i)
        fecha_Actualizar=dicc_fechas.get(fecha_select,0)
        if fecha_Actualizar!=0:
            choferes_fecha.update (fecha_Actualizar)
    return losChoferes.difference(choferes_fecha)
    
def grabarArchivo(fecha,diccionario,losChoferes,n):
    archivo=open("idRuta_fecha.txt","w")
    for id_ruta,dicc_fechas in diccionario.items():
        conjunto_choferes=encontrarChoferes(diccionario,fecha,losChoferes,id_ruta,n)
        archivo.write("Para la ruta "+ id_ruta+" los choferes disponibles para la fecha"+ fecha
        +"hayan manejado "+ str(n)+ " dias anteriores son:\n")
        for chofer in conjunto_choferes:
            archivo.write(chofer+"\n")
    archivo.close()

#losChoferes={"AAQSPTTGL","EVNTAASFL","AGBCCAPMP","SMSNADOPN"}
losChoferes,d=cargarDatos("rutasManejadas2018")
print(d)
grabarArchivo("18-05-2018",d,losChoferes,3)