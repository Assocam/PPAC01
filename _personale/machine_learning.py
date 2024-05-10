
"""ogni record del file ha questa forma
'ingrediente1, ingrediente2, ingrediente3', 4
"""
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

data=pd.read_csv('ricette.csv')
X=data['ingredienti']
Y=data['gradimento']

model=make_pipeline(TfidfVectorizer(), Ridge())  #ChatGPT: mi spieghi questa riga di codice?
#TfidfVectorizer() fa la separazione vettoriale degli ingredienti, ogni ingrediente è elemento numerico della lista

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=27)
model.fit(X_train, Y_train)  #riempie il modello
score=model.score(X_test, Y_test) #testa il modello

nuova_ricetta=["farina, zucchero, uova, burro, cioccolato"]
gradimento_predetto=model.predict(nuova_ricetta)

print(f'punteggio del modello {score}')
print(f'Punteggio predetto per {nuova_ricetta} = {gradimento_predetto}')