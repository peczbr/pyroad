# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 23:24:48 2022

@author: pedro
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score, LeaveOneOut
from sklearn.metrics import mean_squared_error, roc_curve, accuracy_score
from sklearn import preprocessing

df = pd.read_excel('BR12-22.xlsx', usecols="B:T")
df = df.drop(["País","Liga","Temporada","PM","PE","PV","Data","Horário","Res"], axis = 1)
df["Vitória"] = pd.Series(df["GM"]>df["GV"]).astype(int)
df["Empate"] = pd.Series(df["GM"]==df["GV"]).astype(int)
df["Derrota"] = pd.Series(df["GM"]<df["GV"]).astype(int)
le = preprocessing.LabelEncoder()
le.fit(df["Mandante"])
df["Mandante"] = le.transform(df["Mandante"])
df["Visitante"] = le.transform(df["Visitante"])
modelos = [DecisionTreeClassifier(), RandomForestClassifier(), KNeighborsClassifier(), GaussianNB()]
X = df.drop(["GM","GV","Vitória","Empate","Derrota","MaxM","MaxE","MaxV","AvgM","AvgE","AvgV"], axis = 1)
#Classe Vitoria
Y = df["Vitória"]
Xtr, Xteste, Ytr, Yteste = train_test_split(X,Y, test_size = 0.7, random_state=0)
modelo = RandomForestClassifier(n_estimators= 1000, min_samples_leaf = 3, random_state = 0 )
modelo.fit(Xtr, Ytr)
p = modelo.predict(Xteste)
scoreVitoria = accuracy_score(Yteste, p)
#Classe Empate
Y = df["Empate"]
Xtr, Xteste, Ytr, Yteste = train_test_split(X,Y, test_size = 0.7, random_state=0)
modelo = RandomForestClassifier(n_estimators= 1000, min_samples_leaf = 3, random_state = 0 )
modelo.fit(Xtr, Ytr)
p = modelo.predict(Xteste)
scoreEmpate = accuracy_score(Yteste, p)
#Classe Derrota
Y = df["Derrota"]
Xtr, Xteste, Ytr, Yteste = train_test_split(X,Y, test_size = 0.7, random_state=0)
modelo = RandomForestClassifier(n_estimators= 1000, min_samples_leaf = 3, random_state = 0 )
modelo.fit(Xtr, Ytr)
p = modelo.predict(Xteste)
scoreDerrota = accuracy_score(Yteste, p)
print (scoreVitoria)
print (scoreEmpate)
print (scoreDerrota)
#def avaliar_modelo(X, Y, cv, modelo):
    #scores = cross_val_score(modelo, X, Y, scoring = "accuracy", cv=cv, n_jobs=-1)
    #acuracia
    #return scores.mean()
#folds = range(2,21)
#means = list()
#for k in folds:
    #cv = KFold(n_splits=k, shuffle=True, random_state=1)
    #k_mean = avaliar_modelo(X, Y, cv, modelos[1])
    #print('> folds=%d, accuracy=%.3f' % (k, k_mean))
    #means.append(k_mean)