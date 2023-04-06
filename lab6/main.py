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

print("Zadanie 3")
df2 = pd.read_csv('zamowienia.csv', delimiter=';')
print("a")
unique_surnames = df2['Sprzedawca'].unique()
print(unique_surnames)
print("b")
highest_orders = df2['Utarg'].nlargest(5)
print(highest_orders)
print("c")
orders_by_seller = df2['Sprzedawca'].value_counts()
print(orders_by_seller)
print("d")
orders_by_country = df2.groupby('Kraj')['Utarg'].sum()
print(orders_by_country)
print("e")
orders_by_polish_sellers_2005 = df2[(df2['Data zamowienia'].str.contains('2005')) & (df2['Kraj'] == 'Polska')]['Utarg'].sum()
print(orders_by_polish_sellers_2005)
print("f")
mean_order_value_2004 = df2[df2['Data zamowienia'].str.contains('2004')]['Utarg'].mean()
print(mean_order_value_2004)
print("g")
orders_2004 = df2[df2['Data zamowienia'].str.contains('2004')]
orders_2005 = df2[df2['Data zamowienia'].str.contains('2005')]

orders_2004.to_csv('zamowienia_2004.csv', index=False)
orders_2005.to_csv('zamowienia_2005.csv', index=False)