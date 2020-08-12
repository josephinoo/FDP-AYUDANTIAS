
consumo_energia = {
    'Coca Codo Sinclair': {
        'Quito': {'consumos': (400, 432, 213,400, 432, 213,400, 432, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 70,400, 432, 213,400, 432, 213), 'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil': {'consumos': (310, 220, 321, 200,400, 432, 213), 'tarifa': 55},
        'Quito': {'consumos': (400, 432, 587,400, 432, 213,400, 432, 213), 'tarifa': 79},
        'Loja': {'consumos': (50, 32, 32, 40,400, 432, 213,400, 432, 213), 'tarifa': 32}
    }
}
informacion = {
    'costa': ('Guayaquil', 'Manta'),
    'sierra': ('Quito', 'Ambato',"Loja"),
    'oriente': ('Tena', 'Nueva Loja')
}


def total_anual(consumo_energia, planta, ciudad):
    dic_ciudad = consumo_energia[planta][ciudad]
    return sum(dic_ciudad["consumos"])


def total_plantas_ciudad(consumo_energia, ciudad):
    diccionario = dict()
    for planta, dic_planta in consumo_energia.items():
        dic_ciudad = dic_planta.get(ciudad, 0)
        if dic_ciudad != 0:
            diccionario[planta] = total_anual(consumo_energia, planta, ciudad)
    return diccionario


def megavatios_hora(consumo_energia, informacion):
    ciudades = informacion["sierra"]
    total = 0
    for ciudad in ciudades:
        dic_total = total_plantas_ciudad(consumo_energia, ciudad)
        total += sum(dic_total.values())
    return total

def facturacion(consumo_energia):
    archivo=open("facturacion.txt","w")
    archivo.write("Planta,enero,febrero,marzo,abril,mayo,junio\n")
    for planta,dic_planta in consumo_energia.items():
        archivo.write(planta)
        for i in range(6):
            suma=0
            for dic_ciudad in dic_planta.values():
                print(dic_ciudad["consumos"])
                suma+=dic_ciudad["consumos"][i]
                
            archivo.write(","+str(suma))
        archivo.write("\n")
    archivo.close()

facturacion(consumo_energia)
print(megavatios_hora(consumo_energia, informacion))
