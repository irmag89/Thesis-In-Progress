#Importing the libraries
import pandas as pd
import es_core_news_lg

#Declarar variables
sp = es_core_news_lg.load()
AllWordsDataset, DatasetList1, DatasetList2= [], [], [];

#Importing the dataset
#Dataset == Books for Grade
Dataset1 = pd.read_table('All_Word_Books_Primary_1.txt',quoting = 3 , encoding='latin-1')

for i in range(len(Dataset1)):
    DatasetList1.append(Dataset1['Libro1'][i].lower())

len(DatasetList1)

Dataset2 = pd.read_table('All_Word_Books_Primary_2.txt',quoting = 3 , encoding='latin-1')

for i in range(len(Dataset2)):
    DatasetList2.append(Dataset2['Libro1'][i].lower())

len(DatasetList2)


#Comparar
palabras_nuevas=[]
for element in DatasetList2:
    if element not in DatasetList1: 
        palabras_nuevas.append(element)
        
len(palabras_nuevas)

#Almacenar palabras contadas en txt
with open('List_New_Words_1_To_2.txt', 'w') as temp_file:
    for item in  palabras_nuevas:
        temp_file.write("%s\n" % item)

#Borrar el contenido del txt (opcional)
f = open('List_New_Words_1_To_2.txt', 'w')
f.close()

