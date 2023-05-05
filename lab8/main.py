import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#Zad1
x = np.arange(1, 21)
y = 1/x
plt.plot(x, y, label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla x [1,20]")
plt.legend()
plt.axis([1, 20, 0, 1])
plt.grid(True)
plt.show()

#Zad2
x = np.arange(1, 21, 1)
y = 1/x
plt.plot(x, y, 'g-->', label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla x [1,20]")
plt.legend()
plt.axis([0, 20, 0, 1])
plt.grid(True)
plt.show()

#Zad3
x = np.arange(0, 30.1, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, label="sin(x)")
plt.plot(x, z, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres sin(x), cos(x)")
plt.legend()
plt.axis([-0.5, 31.5, -1.1, 1.1])
plt.show()

#Zad4
x = np.arange(0, 30.1, 0.1)
y = np.sin(x) + 2
z = -np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.plot(x, z, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc=1)
plt.axis([-0.5, 31.5, -1.1, 3.1])
plt.show()

#Zad5
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
ds = pd.read_csv(url, names=names)
data = ds.iloc[:, :-1].values
x = data[:,0]
y = data[:,1]
size = np.abs(x - y)
color = np.random.randint(0, 50, len(x))
plt.scatter(x, y, c=color, s=size)
plt.colorbar()
plt.show()

#Zad6
excelPath = 'D:\Repositories\WD_169397_2023\lab7\imiona.xlsx'
df = pd.read_excel(excelPath)

plt.figure(figsize=(20, 6))

plt.subplot(1, 3, 1)
grouped_df_plec = df.groupby('Plec')['Liczba'].sum()
plt.bar(grouped_df_plec.index, grouped_df_plec.values, color=['pink', 'lightblue'])
plt.title('Ilość narodzonych dziewczynek i chłopców')
plt.xlabel('Płeć')
plt.ylabel('Liczba narodzin')

plt.subplot(1, 3, 2)
grouped_df_plec_rok = df.groupby([pd.to_datetime(df['Rok'], format="%Y"), 'Plec'])['Liczba'].sum().unstack()
plt.plot(grouped_df_plec_rok.index, grouped_df_plec_rok['K'], color='red', label='Kobiety')
plt.plot(grouped_df_plec_rok.index, grouped_df_plec_rok['M'], color='blue', label='Mężczyźni')
plt.title('Ilość narodzonych kobiet i mężczyzn w poszczególnych latach')
plt.xlabel('Rok')
plt.ylabel('Liczba narodzin')

plt.subplot(1, 3, 3)
grouped_df_rok = df.groupby(pd.to_datetime(df['Rok'], format='%Y'))['Liczba'].sum()
plt.bar(grouped_df_rok.index.year.astype(str), grouped_df_rok.values, color='green')
plt.title('Suma urodzonych dzieci w każdym roku')
plt.xticks(rotation='vertical')
plt.xlabel('Rok')
plt.ylabel('Liczba narodzin')

plt.subplots_adjust(wspace=0.5)

plt.show()

#Zad7
def rzut_koscia_d6(n):
    wyniki = []
    for i in range(n):
        rzut1 = random.randint(1, 6)
        rzut2 = random.randint(1, 6)
        suma = rzut1 + rzut2
        wyniki.append(suma)
    plt.hist(wyniki, bins=11, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Suma wyników rzutów')
    plt.ylabel('Prawdopodobieństwo')
    plt.title(f'Histogram sum wyników dwóch rzutów kostką d6 ({n} rzutów)')
    plt.grid(True)
    plt.show()
    return wyniki

rzut_koscia_d6(10000)

#Zad8
csvPath = 'D:\Repositories\WD_169397_2023\lab7\zamowienia.csv'
df = pd.read_csv(csvPath, delimiter=';')

total_sales = df.groupby('Sprzedawca')['Utarg'].sum()
percent_sales = total_sales / total_sales.sum() * 100
plt.figure(figsize=(8, 5))
wedges, texts, autotexts = plt.pie(percent_sales, labels=percent_sales.index, autopct='%.1f%%', textprops = dict(color="black"))
plt.setp(autotexts, size=14, weight="bold")
plt.title('Procentowy udział sprzedawców w ogólnej sumie zamówień')
plt.legend(title='Sprzedawcy', bbox_to_anchor=(1.1, 1))
plt.tight_layout()
plt.show()