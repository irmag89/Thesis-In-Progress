import  os

#Declare variables
lista=[]
listFiles=[]
directorio= 'C:\\Tesis tests\\tests\\'

#Funcion ordenar
def ordenar(archivo):
    #Book name
    BookName= archivo

    with open(directorio+BookName, 'r', encoding="utf-8") as temp_file:
        for linea in temp_file.readlines():
            lista.append(linea)
        temp_file.close()

    #Order 
    lista.sort()

    #Save words
    with open(directorio+BookName, 'w', encoding="utf-8") as temp_file:
        for item in lista:
            temp_file.write("%s" % item)
        temp_file.close()

    #Limpiar lista
    lista.clear()
    
with os.scandir(directorio) as carpeta:
    for archivo in carpeta:
         listFiles.append(archivo.name)

for archivo in listFiles:
    ordenar(archivo)

print("Finished!");
