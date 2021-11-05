import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import es_core_news_lg

sp = es_core_news_lg.load()
CountADJ, CountADP, CountADV, CountAUX, CountCONJ,CountCCONJ,CountDET,CountINTJ,CountNOUN,CountNUM,CountPART,CountPRON,CountPROPN,CountPUNCT,CountSCONJ,CountSYM,CountVERB,CountX,CountSPACE=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
LCountADJ, LCountADP, LCountADV, LCountAUX, LCountCONJ,LCountCCONJ,LCountDET,LCountINTJ,LCountNOUN,LCountNUM,LCountPART,LCountPRON,LCountPROPN,LCountPUNCT,LCountSCONJ,LCountSYM,LCountVERB,LCountX,LCountSPACE=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
dataset = pd.read_csv('lms.csv',quoting = 3 , encoding='utf-8')
for i in range(0, 1662):
    
     doc= sp(dataset['LSM'][i])
     POS_counts = doc.count_by(spacy.attrs.POS)

     for k,v in sorted(POS_counts.items()):
         #print(f'{k:{10}}. {doc.vocab[k].text:{2}}: {v}')
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

print("\nadjective=", CountADJ, "\nadposition=",  CountADP,"\nadverb=",  CountADV, "\nauxiliary=", CountAUX,"\nconjunction=",  CountCONJ,"\ncoordinating conjunction=", CountCCONJ,"\ndeterminer=", CountDET,"\ninterjection=", CountINTJ,"\nnoun=", CountNOUN,"\nnumeral=", CountNUM,"\npartical=", CountPART,"\npronoun=", CountPRON,"\nproper noun=", CountPROPN,"\npunctuation=", CountPUNCT,"	\nsubordinating conjunction=", CountSCONJ,"\nsymbol=", CountSYM,"\nverb=", CountVERB,"\nother=", CountX,"\nspace=", CountSPACE)
             
        ## elif token.pos_ == "NOUN":
             
#CountADJ= 0, CountADP= 0, CountADV= 0 , CountAUX= 0, CountCONJ= 0, CountCCONJ= 0, CountDET= 0, CountINTJ= 0, CountNOUN= 0, CountNUM= 0, CountPART= 0, CountPRON= 0 , CountPROPN= 0, CountPUNCT= 0, CountSCONJ= 0, CountSYM= 0 , CountVERB= 0, CountX= 0, CountSPACE= 0;

                 
                 

# obtener todas las etiquetas
all_tags = {w.pos: w.pos_}

##nouns = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]


##################
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Get busy living or get busy dying.")

print(f"{'text':{8}} {'POS':{6}} {'TAG':{6}} {'Dep':{6}} {'POS explained':{20}} {'tag explained'} ")
for token in doc:
print(f'{token.text:{8}} {token.pos_:{6}} {token.tag_:{6}} {token.dep_:{6}} {spacy.explain(token.pos_):{20}} {spacy.explain(token.tag_)}')
##################

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import es_core_news_lg
sp = es_core_news_lg.load()

# Importing the dataset
dataset = pd.read_table('dragon_rojo.txt',quoting = 3 , encoding='utf-8')
dataset
# Cleaning the texts

dataset['Libro1'][2]

#

print("LEMMA:")
print("====================================")

clean_tokens = dataset['Libro1'][2].split()

clean_tokens
total_lemmas=[]
for i in range(len(clean_tokens)):
    sentence7 = sp(clean_tokens[i])
    for word in sentence7:
        print(word.text + '===>', word.lemma_)
        total_lemmas.append(word.lemma_)
        
        
        

print("")
print("")
print("POS:")
print("====================================")

for i in range(len(clean_tokens)):
    sentence7 = sp(clean_tokens[i])
    for word in sentence7:
        print(word.text,  word.pos_)


##################


print("spaCy version: ", spacy.__version__)

print("LEMMA:")
print("====================================")

clean_tokens = ["Mucha", "mano", ",","@", "técnica", "en", "productos"]
total_lemmas=[]
for i in range(len(clean_tokens)):
    sentence7 = sp(clean_tokens[i])
    for word in sentence7:
        print(word.text + '  ===>', word.lemma_)
        lemmas=word.lemma_
        total_lemmas.append(lemmas)

print("")
print("")
print("POS:")
print("====================================")

for i in range(len(clean_tokens)):
    sentence7 = sp(clean_tokens[i])
    for word in sentence7:
        print(word.text,  word.pos_)

#######################
























import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#libreria para eiminar conjugaciones y llevar a la raiz, lematizaqar y sin conectores
from nltk.stem import PorterStemmer
corpus = []
review = re.sub('[^a-zA-Z]\d', ' ', dataset['Libro1'][2])

review

review = review.lower()
review = review.split()
ps = PorterStemmer()
review = [ps.stem(word) for word in review if not word in set(stopwords.words('spanish'))]
review = ' '.join(review)
review



###########################################



def lunes():
	print('lunes')

def martes():
	print('martes')

def miercoles():
	print('miércoles')

def jueves():
	print('jueves')

def viernes():
	print('viernes')

def sabado():
	print('sábado')

def domingo():
	print('domingo')

def error():
	print('error')

switch_semana = {
	1: lunes,
	2: martes,
	3: miercoles,
	4: jueves,
	5: viernes,
	6: sabado,
	7: domingo
}

dia = 8

#tomamos la función asociada a la variable y la invocamos
switch_semana.get(dia, error)()

CountADJ=0;
CountADP= 0;
CountADV= 0;
CountAUX= 0;
CountCONJ= 0;
CountCCONJ= 0;
CountDET= 0;
CountINTJ= 0;
CountNOUN= 0;
CountNUM= 0;
CountPART= 0;
CountPRON= 0;
CountPROPN= 0;
CountPUNCT= 0;
CountSCONJ= 0;
CountSYM= 0;
CountVERB= 0;
CountX= 0;
CountSPACE= 0;