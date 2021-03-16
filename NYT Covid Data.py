#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:05:39 2020

@author: mmcginnes
1AM Main Branch
"""
# %%

import pandas as pd
from datetime import date 
# %%

states = ('Virginia','Maryland','District of Columbia','Florida')
df=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
print(df.head())
df = df[df['state'].isin(states)]
df.sort_values(by=['fips','state','county','date'], inplace=True)

newcases = []
for row in range(0,len(df)):
    if row == 0:
       newcases.append(df.iloc[row]['cases'])
    elif df.iloc[row]['fips'] == df.iloc[row-1]['fips']:
        newcases.append (df.iloc[row]['cases']-df.iloc[row-1]['cases'])
    else:
        newcases.append(df.iloc[row]['cases'])
#    df2.loc[row]['New cases'] =  result
#    print (newcases)       
df['new cases'] = newcases
#print(df.describe())
    
newdeaths = []
for row in range(0,len(df)):
    if row == 0:
       newdeaths.append(df.iloc[row]['deaths'])
    elif df.iloc[row]['fips'] == df.iloc[row-1]['fips']:
        newdeaths.append (df.iloc[row]['deaths']-df.iloc[row-1]['deaths'])
    else:
        newdeaths.append(df.iloc[row]['deaths'])
#    df2.loc[row]['New cases'] =  result
#    print (newcases)       
df['new deaths'] = newdeaths
#print(df.describe())

#print (df.head)
df.to_csv('C:/Users/mmcginnes/Documents/GitHub/Covid-19.1/NYTCovid19.csv', index=False)
print(df.tail())
print(date.today())
print (df.date.max())

#for row in range(len(df2)):
#    print (df2.iloc[row],['New cases'])
#C:\Users\mmcginnes\Documents\GitHub\Covid-19.1

