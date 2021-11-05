#Importing the libraries
import pandas as pd
import es_core_news_lg

#Declarar variables
sp = es_core_news_lg.load()
AllWordsDataset, DatasetList1, DatasetList2= [], [], [];

#Importing the dataset
Dataset1 = pd.read_table('Civica_1_Words.txt',quoting = 3 , encoding='latin-1')

for i in range(len(Dataset1)):
    DatasetList1.append(Dataset1['Libro1'][i])

Dataset2 = pd.read_table('Lecturas_2_Words.txt',quoting = 3 , encoding='latin-1')

for i in range(len(Dataset2)):
    DatasetList2.append(Dataset2['Libro1'][i])

#Join datasets
AllWordsDataset= DatasetList1 + DatasetList2 

#Eliminar Palabras repetidas
len(AllWordsDataset)
total_lemmas_Sin_Repeticiones=[]
for element in AllWordsDataset:
    if element not in total_lemmas_Sin_Repeticiones: 
        total_lemmas_Sin_Repeticiones.append(element)
len(total_lemmas_Sin_Repeticiones)

#Almacenar palabras contadas en txt
with open('All_Word_Books_Primary_1.txt', 'w') as temp_file:
    for item in  total_lemmas_Sin_Repeticiones:
        temp_file.write("%s\n" % item)

