a=open("archivo_prueba2.txt",mode="a")
a.write("LOLA, Loja\n")
a.write("LOLA, MEJIA\n")
a=open("archivo_prueba_2.0.txt",mode="a")

archivo=open("bank.csv",mode="r")
print(archivo.readline())
print(archivo.readline())
print(len(archivo.readlines()))