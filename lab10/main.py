import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Zad1():
    df = pd.read_excel('imiona.xlsx')
    k_names = df[df['Imie'].str[0]=='K']
    unique_k_names = k_names['Imie'].nunique()
    print("Amount of unique names starting with letter 'K':", unique_k_names)

def Zad2():
    df = pd.read_excel('imiona.xlsx')

    name_counts = df.groupby(['Imie', 'Plec'])['Liczba'].sum().reset_index()

    most_common_male_name = name_counts[name_counts['Plec'] == 'M'].nlargest(1, 'Liczba')
    most_common_male_name = most_common_male_name.iloc[0]['Imie']
    print("Most common male name:", most_common_male_name)

    most_common_female_name = name_counts[name_counts['Plec'] == 'K'].nlargest(1, 'Liczba')
    most_common_female_name = most_common_female_name.iloc[0]['Imie']
    print("Most common female name:", most_common_female_name)


def Zad3():
    fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(10,6))
    fig.suptitle('Liczba  narodzin w latach 2010-2015')
    ax1.set_title('Wykres w pandasie')
    ax2.set_title('Wykres w seaborn')
    df = pd.read_excel('imiona.xlsx')
    #filtrowanie po kolumnie 'Rok' (2010-2015)
    data = df[(df['Rok'] >= 2010) & (df['Rok'] <= 2015)]
    data_grouped = data.groupby('Plec')['Liczba'].sum()
    data_grouped.plot.bar(ax=ax1)
    ax1.legend()
    sns.barplot(data=data, x='Plec', y='Liczba', estimator=sum, errorbar=None, ax=ax2)
    plt.show()


Zad1()
Zad2()
Zad3()
