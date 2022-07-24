#Importing the libraries
import pandas as pd
import es_core_news_lg

#Declare variables
sp = es_core_news_lg.load()
AllWordsDataset=[];

#Read all books of the grade
book1= 'artistica_6_LR';
book2= 'espanol_6_1_LR';
book3= 'espanol_6_2_LR';
book4= 'historia_6_LR';
book5= 'matematicas_6_LR';
book6= 'civica_6_LR';
book7= 'geografia_6_LR';
book8= 'naturales_6_LR';

#Save set of words not repetead in the grade in:
savebookin= 'All_Word_Books_Primary_6';

#Books for Grade ==> Dataset 
#Importing dataset 1
Dataset1 = pd.read_table(book1+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset1)):
    AllWordsDataset.append(Dataset1['words'][i])
    
#Importing dataset 2
Dataset2 = pd.read_table(book2+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset2)):
    AllWordsDataset.append(Dataset2['words'][i])

#Importing dataset 3
Dataset3 = pd.read_table(book3+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset3)):
    AllWordsDataset.append(Dataset3['words'][i])

#Importing dataset 4
Dataset4 = pd.read_table(book4+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset4)):
    AllWordsDataset.append(Dataset4['words'][i])

#Importing dataset 5
Dataset5 = pd.read_table(book5+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset5)):
    AllWordsDataset.append(Dataset5['words'][i])

#Importing dataset 6
Dataset6 = pd.read_table(book6+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset6)):
    AllWordsDataset.append(Dataset6['words'][i])

#Importing dataset 7
Dataset7 = pd.read_table(book7+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset7)):
    AllWordsDataset.append(Dataset7['words'][i])

#Importing dataset 8
Dataset8 = pd.read_table(book8+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset8)):
    AllWordsDataset.append(Dataset8['words'][i])

#Delete repeated words from the set of words in the grade
len(AllWordsDataset)
AllWordsDataset_Not_Repeated=[]
for element in AllWordsDataset:
    if element not in AllWordsDataset_Not_Repeated: 
        AllWordsDataset_Not_Repeated.append(element)

#order
AllWordsDataset_Not_Repeated.sort()

#Save set of words in the grade list
with open(savebookin +'_LR.txt', 'w', encoding="utf-8") as temp_file:
    for item in  AllWordsDataset_Not_Repeated:
        temp_file.write("%s\n" % item)

#Save results
with open(savebookin +'_text.txt', 'w', encoding="utf-8") as temp_file:
    temp_file.write("Total words in grade: " + str(len(AllWordsDataset_Not_Repeated)))

#Print results in console
print("Total words in grade: " + str(len(AllWordsDataset_Not_Repeated)))
print("Finished!");