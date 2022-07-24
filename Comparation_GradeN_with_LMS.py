#Importing the libraries
import pandas as pd
import es_core_news_lg

#Declare variables
sp = es_core_news_lg.load()
AllWordsDataset, DatasetList1, DatasetList2, DatasetList3= [], [], [], [];

#Read texts
book1= 'LMS_LR'; #LMS text
book2= 'All_Word_Books_Primary_6_LR'; #Grade text

#Read set of learned words in previous grades of:
book3= 'All_Learned_Words_LMS_0_1_2_3_4_5_LR';

#Save new set of learned words(including this grade):
saveAll_LearnedWordsIn= 'All_Learned_Words_LMS_0_1_2_3_4_5_6';

#Save exclusive words list in:
saveExclusiveWordsIn= 'words_exclusive_6_LMS';

#Save new words list in:
saveNewWordsIn= 'words_new_0_1_2_3_4_5_to_6_LMS';

#Save results of exclusive words, new words and new all words learned list in:
saveTotalResultsIn= 'words_new_exclusive_totalWordsLearned_0_1_2_3_4_5_to_6_LMS';

#importing LMS
Dataset1 = pd.read_table(book1+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset1)):
    DatasetList1.append(Dataset1['words'][i].lower())

len(DatasetList1)

#importing Grade
Dataset2 = pd.read_table(book2+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset2)):
    DatasetList2.append(Dataset2['words'][i].lower())

len(DatasetList2)

#importing set of words learned in previous grades
Dataset3 = pd.read_table(book3+'.txt',quoting = 3 , encoding="utf-8")

for i in range(len(Dataset3)):
    DatasetList3.append(Dataset3['words'][i].lower())

len(DatasetList3)

#Compare LMS with the grade for get exclusive words
words_exclusive_LMS=[]
for element in DatasetList2:
    if element in DatasetList1: 
        words_exclusive_LMS.append(element)
        
#Compare LMS with set of words learned in previous grades 
words_new_N0_to_N1_LMS=[]
for element in words_exclusive_LMS:
    if element not in DatasetList3: 
        #add new word detected to "new words list"
        words_new_N0_to_N1_LMS.append(element)
        #add new word detected to "all learned words list"
        DatasetList3.append(element)

#order
words_new_N0_to_N1_LMS.sort()
words_exclusive_LMS.sort()
DatasetList3.sort()
        
#Save new words
with open(saveNewWordsIn+'_LR.txt', 'w', encoding="utf-8") as temp_file:
    for item in words_new_N0_to_N1_LMS:
        temp_file.write("%s\n" % item)
        
#Save exclusive words
with open(saveExclusiveWordsIn+'_LR.txt', 'w', encoding="utf-8") as temp_file:
    for item in words_exclusive_LMS:
        temp_file.write("%s\n" % item)

#Save all learned words for the next analysis
with open(saveAll_LearnedWordsIn+'_LR.txt', 'w', encoding="utf-8") as temp_file:
    for item in DatasetList3:
        temp_file.write("%s\n" % item)

#Save results about exclusive, new and all learned words
with open(saveTotalResultsIn+'_text.txt', 'w', encoding="utf-8") as temp_file:
    temp_file.write("Exclusive words between grade and LMS: " + str(len(words_exclusive_LMS)) + '\n'+"New words(not before seen in previous degrees): " + str(len(words_new_N0_to_N1_LMS))+ '\n'+"Total words learned so far: " + str(len(DatasetList3)))

#Print results in console
print("Exclusive words between grade and LMS: " + str(len(words_exclusive_LMS)) + '\n'+"New words(not before seen in previous degrees): " + str(len(words_new_N0_to_N1_LMS))+ '\n'+"Total words learned so far: " + str(len(DatasetList3)))
print("Finished!");