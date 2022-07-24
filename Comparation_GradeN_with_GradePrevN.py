#Importing the libraries
import pandas as pd
import es_core_news_lg

#Declare variables
sp = es_core_news_lg.load()
AllWordsDataset, DatasetList1, DatasetList2= [], [], [];

#Read Grade N of:
book1= 'All_Word_Books_Primary_6_LR'; 

#Read set of words learned in previous grades of:
book2= 'All_Learned_Words_0_1_2_3_4_5_LR';

#Save new set of learned words(including this grade):
saveAll_LearnedWordsIn= 'All_Learned_Words_0_1_2_3_4_5_6';

#Save new words in:
saveNewWordsIn= 'words_new_0_1_2_3_4_5_to_6';

#Save the results of new words and all learned words in:
saveTotalResultsIn= 'words_new_totalWordsLearned_0_1_2_3_4_5_6';

#Importing the dataset
Dataset1 = pd.read_table(book1+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset1)):
    DatasetList1.append(Dataset1['words'][i].lower())

len(DatasetList1)

#Import set of learned words
Dataset2 = pd.read_table(book2+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset2)):
    DatasetList2.append(Dataset2['words'][i].lower())

len(DatasetList2)

#Compare set of words learned with grade 
words_new_N0_to_N1=[]
for element in DatasetList1:
    if element not in DatasetList2: 
        #add new word detected to "new words list"
        words_new_N0_to_N1.append(element)
        #add new word detected to "all learned words list"
        DatasetList2.append(element)

#order
words_new_N0_to_N1.sort()
DatasetList2.sort()

#Save new words
with open(saveNewWordsIn+'_LR.txt', 'w', encoding="utf-8") as temp_file:
    for item in words_new_N0_to_N1:
        temp_file.write("%s\n" % item)
        
#Save all learned words for the next analysis
with open(saveAll_LearnedWordsIn+'_LR.txt', 'w', encoding="utf-8") as temp_file:
    for item in DatasetList2:
        temp_file.write("%s\n" % item)

#Save results about new and all learned words
with open(saveTotalResultsIn+'_text.txt', 'w', encoding="utf-8") as temp_file:
    temp_file.write('\n'+"New words(not before seen in previous degrees): " + str(len(words_new_N0_to_N1))+ '\n'+"Total words learned so far: " + str(len(DatasetList2)))

#Print results in console
print('\n'+"New words(not before seen in previous degrees): " + str(len(words_new_N0_to_N1))+ '\n'+"Total words learned so far: " + str(len(DatasetList2)))
print("Finished!");