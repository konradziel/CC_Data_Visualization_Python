import numpy as np
import pandas as pd

print("Zadanie 1")
df = pd.read_excel('imiona.xlsx')
print(df)

print("Zadanie 2")
print("a")
print(df[df['Liczba']>1000])
print("b")
print(df[df['Imie'] == 'KONRAD'])
print("c")
print(df['Liczba'].sum())
print("d")
year_group = df.groupby('Rok')
print(year_group.sum(numeric_only=True))
print("e")
e = df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
print(e['Liczba'].sum())
print("f")
sex_group = df.groupby('Plec')
print(sex_group['Liczba'].sum())
print("g")
s = (df.groupby(['Plec', 'Imie'])['Liczba'].sum())
print(s.loc[s.groupby('Plec').idxmax()])
print("h")
s = (df.groupby(['Plec', 'Imie', 'Rok'])['Liczba'].sum())
print(s.loc[s.groupby(['Plec', 'Rok']).idxmax()])
