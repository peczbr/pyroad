# -*- coding: utf-8 -*-
"""
@author: pecz
#DATA-BASE: https://www.football-data.co.uk/brazil.php
#DATA: BRAZIL FOOTBALL LEAGUE DATA - 2012 to 2022 records
#The CODE make some DATA modifications and brought the DATA to an brazillian base in EXCEL
#UTC to UTC-3 (America/Sao_Paulo)
"""
import pandas as pd
import datetime as dt
import pytz as pz
from zoneinfo import ZoneInfo as zf

df = pd.read_excel('BRA.xlsx')
#Padronizando nomes dos clubes
df = df.apply(lambda x: x.replace("Atletico-PR","Athletico-PR"))
df = df.apply(lambda x: x.replace("America MG","America-MG"))
df = df.apply(lambda x: x.replace("Botafogo RJ","Botafogo-RJ"))
df = df.apply(lambda x: x.replace("Flamengo RJ","Flamengo"))
df = df.apply(lambda x: x.replace("Chapecoense-SC","Chapecoense"))
df = df.apply(lambda x: x.replace("Atletico GO","Atletico-GO"))
df = df.apply(lambda x: x.replace("H","V"))
df = df.apply(lambda x: x.replace("D","E"))
df = df.apply(lambda x: x.replace("A","D"))
df = df.apply(lambda x: x.replace("Brazil","Brasil"))

#Contador
c = -1
tam = len(df["Date"])-1
#Acertando as datas para fuso horário UTC-3 (Sao_Paulo)
while c !=  tam:
    c = c + 1
    w = df["Date"][c]
    z = w.to_pydatetime()
    ano = z.year
    mes = z.month
    dia = z.day
    time = df["Time"][c]
    dato = dt.datetime(ano,mes,dia,time.hour,time.minute)
    data = dato.replace(tzinfo=zf("Europe/London"))
    #convertendo hora
    fuso2 = pz.timezone("America/Sao_Paulo")
    cv = data.astimezone(fuso2)
    dati = dt.datetime(cv.year,cv.month,cv.day,cv.hour,cv.minute)    
    horario = dt.time(dati.hour,dati.minute)
    data_j = dt.datetime(dati.year,dati.month,dati.day)
    df["Time"][c] = horario
    df["Date"][c] = data_j
    
df.to_excel("BR12-22.xlsx")
 
