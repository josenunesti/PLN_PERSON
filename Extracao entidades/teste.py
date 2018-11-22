import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load('modelo_rodrigo.md')

doc = nlp(u"""0017310-16.2017.4.03.6301 - 9ª VARA GABINETE - SENTENÇA SEM RESOLUÇÃO DE MÉRITO Nr. 2017/6301097946
AUTOR: MICHELE MARTINS GONCALVIS LOARES (SP393059 - RICARDO BARBOZA)
RÉU: INSTITUTO NACIONAL DO SEGURO SOCIAL - I.N.S.S. (PREVID) (SP172114 - HERMES ARRAIS ALENCAR)""")

for X in doc.ents:
    print((X, X.label_, X)) 
    #print((X, X.ent_iob_, X.ent_type_))
    #print( "{} => {}".format(X.text, X.label_))

#print([(X, X.ent_iob_, X.ent_type_) for X in doc])
