# -- coding: utf-8 --
"""
Created on Tue Nov 30 14:27:51 2021

@author: franc
"""

#Importing the libraries
import pandas as pd
import spacy
import es_core_news_lg

#Declare variables
sp = es_core_news_lg.load()
CountADJ, CountADP, CountADV, CountAUX, CountCONJ, CountCCONJ,CountDET,CountINTJ,CountNOUN,CountNUM,CountPART,CountPRON,CountPROPN,CountPUNCT,CountSCONJ,CountSYM,CountVERB,CountX,CountSPACE=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
LCountADJ, LCountADP, LCountADV, LCountAUX, LCountCONJ,LCountCCONJ,LCountDET,LCountINTJ,LCountNOUN,LCountNUM,LCountPART,LCountPRON,LCountPROPN,LCountPUNCT,LCountSCONJ,LCountSYM,LCountVERB,LCountX,LCountSPACE=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
total_lemmas=[]
print("charging 10%...")

#Book name
BookName= 'words_new_0_1_2_3_4_5_to_6_LMS_LR';

#Importing the dataset
dataset = pd.read_table(BookName +'.txt',quoting = 3 , encoding='utf-8')
print("charging 20%...")
for index in range(len(dataset)):
    #lemmatize
    total_lemmas.append(str(dataset['words'][index]))

#Count and filter words
print("charging 70%...")
for e in range(len(total_lemmas)):
    doc= sp(total_lemmas[e])
    POS_counts = doc.count_by(spacy.attrs.POS)
    for k,v in sorted(POS_counts.items()):
        if doc.vocab[k].text == "ADJ":
            CountADJ = CountADJ + 1;
            LCountADJ.append(doc.text)
        elif doc.vocab[k].text == "ADP":
            CountADP = CountADP + 1;
            LCountADP.append(doc.text)
        elif doc.vocab[k].text == "ADV":
            CountADV = CountADV + 1;
            LCountADV.append(doc.text)
        elif doc.vocab[k].text == "AUX":
            CountAUX = CountAUX + 1;
            LCountAUX.append(doc.text)
        elif doc.vocab[k].text == "CONJ":
            CountCONJ = CountCONJ + 1;
            LCountCONJ.append(doc.text)
        elif doc.vocab[k].text == "CCONJ":
            CountCCONJ = CountCCONJ + 1;
            LCountCCONJ.append(doc.text)
        elif doc.vocab[k].text == "DET":
            CountDET = CountDET + 1;
            LCountDET.append(doc.text)
        elif doc.vocab[k].text == "INTJ":
            CountINTJ = CountINTJ + 1;
            LCountINTJ.append(doc.text)
        elif doc.vocab[k].text == "NOUN":
            CountNOUN = CountNOUN + 1;
            LCountNOUN.append(doc.text)
        elif doc.vocab[k].text == "NUM":
            CountNUM = CountNUM + 1;
            LCountNUM.append(doc.text)
        elif doc.vocab[k].text == "PART":
            CountPART = CountPART + 1;
            LCountPART.append(doc.text)
        elif doc.vocab[k].text == "PRON":
            CountPRON = CountPRON + 1;
            LCountPRON.append(doc.text)
        elif doc.vocab[k].text == "PROPN":
            CountPROPN = CountPROPN + 1;
            LCountPROPN.append(doc.text)
        elif doc.vocab[k].text == "PUNCT":
            CountPUNCT = CountPUNCT + 1;
            LCountPUNCT.append(doc.text)
        elif doc.vocab[k].text == "SCONJ":
            CountSCONJ = CountSCONJ + 1;
            LCountSCONJ.append(doc.text)
        elif doc.vocab[k].text == "SYM":
            CountSYM = CountSYM + 1;
            LCountSYM.append(doc.text)
        elif doc.vocab[k].text == "VERB":
            CountVERB = CountVERB + 1;
            LCountVERB.append(doc.text)
        elif doc.vocab[k].text == "X":
            CountX = CountX + 1;
            LCountX.append(doc.text)
        elif doc.vocab[k].text == "SPACE":
            CountSPACE = CountSPACE + 1;
            LCountSPACE.append(doc.text)
            
#Concatenate lists to filter
ListFiltered= LCountNOUN + LCountVERB + LCountAUX;

#Save types of words NOUN
with open(BookName +'_LR_NOUN.txt', 'w', encoding="utf-8") as temp_file:
    for item in  LCountNOUN:
        temp_file.write("%s\n" % item)
temp_file.close()

#Save types of words VERB
with open(BookName +'_LR_VERB.txt', 'w', encoding="utf-8") as temp_file:
    for item in  LCountVERB:
        temp_file.write("%s\n" % item)
temp_file.close()

#Save types of words AUX VERB
with open(BookName +'_LR_AUX.txt', 'w', encoding="utf-8") as temp_file:
    for item in  LCountAUX:
        temp_file.write("%s\n" % item)
temp_file.close()

#Save results
with open(BookName +'_text.txt', 'w', encoding="utf-8") as temp_file:
    temp_file.write('Results'+'\n' + 'adjective= ' + str(CountADJ) + '\n'+ 'adposition= ' + str(CountADP) + '\n'+ 'adverb= ' +  str(CountADV) + '\n' + 'auxiliary= '+ str(CountAUX) +'\n' + 'conjunction= '+ str(CountCONJ) + '\n' + 'coordinating conjunction= '+ str(CountCCONJ)+'\n'+'determiner= '+ str(CountDET) + '\n'+'interjection= '+ str(CountINTJ)+ '\n'+'noun= ' + str(CountNOUN) +'\n'+'numeral= '+ str(CountNUM)+'\n'+'partical= '+ str(CountPART)+'\n'+'pronoun= '+ str(CountPRON) + '\n'+ 'proper noun= '+ str(CountPROPN)+'\n'+ 'punctuation= '+ str(CountPUNCT)+'\n'+'subordinating conjunction= '+ str(CountSCONJ)+'\n'+'symbol= '+ str(CountSYM) +'\n' + 'verb= '+ str(CountVERB) +'\n'+ 'other=' + str(CountX)+'\n'+'space= '+ str(CountSPACE))      

temp_file.close()

#Print results in console
print("charging 100%...")
print("\nadjective=", CountADJ, "\nadposition=",  CountADP,"\nadverb=",  CountADV, "\nauxiliary=", CountAUX,"\nconjunction=",  CountCONJ,"\ncoordinating conjunction=", CountCCONJ,"\ndeterminer=", CountDET,"\ninterjection=", CountINTJ,"\nnoun=", CountNOUN,"\nnumeral=", CountNUM,"\npartical=", CountPART,"\npronoun=", CountPRON,"\nproper noun=", CountPROPN,"\npunctuation=", CountPUNCT,"	\nsubordinating conjunction=", CountSCONJ,"\nsymbol=", CountSYM,"\nverb=", CountVERB,"\nother=", CountX,"\nspace=", CountSPACE)      
print("Finished!");
