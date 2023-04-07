import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx')
print('Zadanie 1')
births_per_year = df.groupby('Rok')['Liczba'].sum()
plt.plot(births_per_year.index, births_per_year.values)
plt.title('Liczba urodzeń na rok')
plt.xlabel('Rok')
plt.ylabel('Liczba urodzeń')
plt.show()

print('Zadanie 2')
births_by_gender = df.groupby('Plec')['Liczba'].sum()
plt.bar(births_by_gender.index, births_by_gender.values)
plt.title('Liczba urodzeń chłopców i dziewczynek')
plt.xlabel('Płeć')
plt.ylabel('Liczba urodzeń')
plt.show()

print('Zadanie 3')
last_5_years = df[df['Rok'] >= 2013]
births_by_gender = last_5_years.groupby('Plec')['Liczba'].sum()
plt.pie(births_by_gender.values, labels=births_by_gender.index, autopct='%1.1f%%')
plt.title('Liczba urodzeń chłopców i dziewczynek w ostatnich 5 latach')
plt.show()

print('Zadanie 4')
df2 = pd.read_csv('zamowienia.csv', delimiter = ';')
orders_by_seller = df2.groupby('Sprzedawca')['idZamowienia'].count()
plt.bar(orders_by_seller.index, orders_by_seller.values)
plt.title('Ilość zamówień przez sprzedawców')
plt.xlabel('Sprzedawca')
plt.ylabel('Liczba zamówień')
plt.show()