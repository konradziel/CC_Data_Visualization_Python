from turtledemo.chaos import g

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_imiona = pd.read_excel('imiona.xlsx')
df_zamowienia = pd.read_csv('zamowienia.csv', delimiter=';')

def Zad1_7():
    dzieciRok = df_imiona.groupby(pd.to_datetime(df_imiona['Rok'], format="%Y"))['Liczba'].sum()
    plt.plot(dzieciRok.index, dzieciRok.values)
    plt.title('Liczba urodzeń na rok')
    plt.xlabel('Rok')
    plt.ylabel('Liczba urodzeń')
    plt.show()

def Zad2_7():
    dzieciPlec = df_imiona.groupby('Plec')['Liczba'].sum()
    plt.bar(dzieciPlec.index, dzieciPlec.values)
    plt.title('Liczba urodzeń')
    plt.xlabel('Plec')
    plt.ylabel('Liczba urodzen')
    plt.show()

def Zad3_7():
    dzieci5Lat = df_imiona[df_imiona['Rok'] >= 2013]
    dzieciPlec = dzieci5Lat.groupby('Plec')['Liczba'].sum()
    plt.pie(dzieciPlec.values, labels=dzieciPlec.index, autopct='%1.1f%%')
    plt.title('Liczba urodzeń chłopców i dziewczynek w ostatnich 5 latach')
    plt.show()

def Zad4_7():
    iloscZamowien = df_zamowienia.groupby('Sprzedawca')['idZamowienia'].count()
    plt.bar(iloscZamowien.index, iloscZamowien.values)
    plt.title('Ilosc zamowien sprzedawcy')
    plt.xlabel('Sprzedawcy')
    plt.ylabel('Liczba zamowien')
    plt.xticks(rotation=30, ha='right')
    plt.show()

def Zad1_10():
    x = np.linspace(1, 20, 100)
    y = 1/x
    plt.plot(x, y, label="f(x)=1/x")
    plt.ylabel('f(x)')
    plt.xlabel('x')
    z = max(x)
    plt.axis([1, z, 0, 1])
    plt.legend()
    plt.grid(True)
    plt.show()

def Zad2_10():
    x = np.linspace(1, 20, 20)
    y = 1 / x
    plt.plot(x, y, 'g-->', label="f(x)=1/x")
    plt.ylabel('f(x)')
    plt.xlabel('x')
    z = max(x)
    plt.axis([1, z, 0, 1])
    plt.legend()
    plt.grid(True)
    plt.show()

def Zad3_10():
    x = np.arange(0, 30.1, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, 'g', label='sin(x)')
    plt.plot(x, z, 'r', label='cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0, 30, -1.1, 1.1])
    plt.legend()
    plt.show()

def Zad4_10():
    x = np.arange(0, 30.1, 0.1)
    y = np.sin(x) + 2
    z = -np.sin(x)
    plt.plot(x, y, color='c', label='sin(x+2)')
    plt.plot(x, z, color='y', label='-sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([-1, 31, -1.3, 3.3])
    plt.xticks([0, 5, 10, 15, 20, 25, 30])
    plt.yticks([-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
    plt.legend(loc=1)
    plt.show()

def Zad5_10():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
    ds = pd.read_csv(url, names=names)
    data = ds.iloc[:, :-1].values
    x = data[:,0]
    y = data[:,1]
    size = abs(x-y)
    color = np.random.randint(0, 50, len(x))
    plt.scatter(x, y, c=color, s=size)
    plt.colorbar()
    plt.show()

def Zad6_10():
    plt.figure(figsize=(20, 6))
    plt.subplot(1, 3, 1)
    narodziny = df_imiona.groupby('Plec')['Liczba'].sum()
    plt.bar(narodziny.index, narodziny.values, color=['pink', 'lightblue'])
    plt.xlabel('Płeć')
    plt.ylabel('Liczba narodzin')
    plt.title('Liczba urodzeń dzieci po płci')

    plt.subplot(1, 3, 2)
    narodzinyRok = df_imiona.groupby(['Rok', 'Plec'])['Liczba'].sum().unstack()
    plt.plot(narodzinyRok.index, narodzinyRok['K'], color='red', label='Kobiety')
    plt.plot(narodzinyRok.index, narodzinyRok['M'], color='blue', label='Mężczyźni')
    plt.title('Ilość narodzonych kobiet i mężczyzn w poszczególnych latach')
    plt.xlabel('Rok')
    plt.ylabel('Liczba narodzin')
    years = np.linspace(min(narodzinyRok.index), max(narodzinyRok.index), narodzinyRok.index.nunique())
    plt.xticks(years, rotation='vertical')

    plt.subplot(1, 3, 3)
    narodzinyRokOnly = df_imiona.groupby('Rok')['Liczba'].sum()
    print(narodzinyRokOnly)
    plt.bar(narodzinyRokOnly.index, narodzinyRokOnly.values)
    plt.title('Ilość narodzonych dzieci rocznie')
    plt.xlabel('Rok')
    plt.ylabel('Liczba narodzin')
    years = np.linspace(min(narodzinyRokOnly.index), max(narodzinyRokOnly.index), narodzinyRokOnly.index.nunique())
    plt.xticks(years, rotation='vertical')

    plt.tight_layout()
    plt.show()

def Zad7_10():
    def Rzut(n):
        wyniki = []
        for i in range(n):
            rzut1 = np.random.randint(1, 7)
            rzut2 = np.random.randint(1, 7)
            suma = rzut1 + rzut2
            wyniki.append(suma)

        plt.hist(wyniki, bins=11, facecolor='g', alpha=0.75, density=True)
        plt.xlabel('Suma wyników rzutów')
        plt.ylabel('Prawdopodobieństwo')
        plt.title(f'Histogram sum wyników dwóch rzutów kostką d6 ({n} rzutów)')
        plt.grid(True)
        plt.show()
        return wyniki

    Rzut(10000)

def Zad8_10():
    sprzedawcySumy = df_zamowienia.groupby('Sprzedawca')['Utarg'].sum()
    percent = (sprzedawcySumy/sprzedawcySumy.sum()) * 100
    plt.figure(figsize=(8, 5))
    wedges, texts, autotexts = plt.pie(percent, labels=percent.index, autopct='%.1f%%', textprops=dict(color='black'))
    plt.setp(autotexts, size=14, weight="bold")
    plt.title('Procentowy udział sprzedawców w ogólnej sumie zamówień')
    plt.legend(title='Sprzedawcy', bbox_to_anchor=(1.1, 1))
    plt.tight_layout()
    plt.show()

def Zad1_12():
    imionaNaK = df_imiona[df_imiona['Imie'].str[0]=='K']
    imionaUnNaK = imionaNaK['Imie'].nunique()
    print("Amount of unique names starting with letter 'K':", imionaUnNaK)

def Zad2_12():
    imiona = df_imiona.groupby(['Plec','Imie'])['Liczba'].sum().reset_index()
    imieK = imiona[imiona['Plec']=='K'].nlargest(1, 'Liczba')
    imieK = imieK.iloc[0]['Imie']

    imiona = df_imiona.groupby(['Plec', 'Imie'])['Liczba'].sum().reset_index()
    imieM = imiona[imiona['Plec'] == 'M'].nlargest(1, 'Liczba')
    imieM = imieM.iloc[0]['Imie']
    print("Female name:", imieK)
    print("Male name:", imieM)

def Zad3_12():
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 6))
    fig.suptitle('Liczba  narodzin w latach 2010-2015')
    ax1.set_title('Wykres w pandasie')
    ax2.set_title('Wykres w seaborn')
    df = pd.read_excel('imiona.xlsx')
    # filtrowanie po kolumnie 'Rok' (2010-2015)
    data = df[(df['Rok'] >= 2010) & (df['Rok'] <= 2015)]
    data_grouped = data.groupby('Plec')['Liczba'].sum()
    data_grouped.plot.bar(ax=ax1)
    ax1.legend()
    sns.barplot(data=data, x='Plec', y='Liczba', estimator=sum, errorbar=None, ax=ax2)
    plt.show()

#Zad1_7()
#Zad2_7()
#Zad3_7()
#Zad4_7()
#Zad1_10()
#Zad2_10()
#Zad3_10()
#Zad4_10()
#Zad5_10()
#Zad6_10()
#Zad7_10()
#Zad8_10()
#Zad1_12()
#Zad2_12()
Zad3_12()