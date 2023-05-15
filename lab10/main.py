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
    df = pd.read_excel('imiona.xlsx')

    df = df[(df['Rok'] >= 2010) & (df['Rok'] <= 2015)]

    grouped_data = df.groupby(['Rok', 'Plec']).size().reset_index(name='Liczba dzieci')
    plt.figure(figsize=(12, 5))
    #Pandas
    plt.subplot(1, 2, 1)
    plt.title('Wykres w pandasie')
    plt.bar(grouped_data[grouped_data['Plec'] == 'K']['Rok'],
            grouped_data[grouped_data['Plec'] == 'K']['Liczba dzieci'], label='K', width=0.35)
    plt.bar(grouped_data[grouped_data['Plec'] == 'M']['Rok'] + 0.35,
            grouped_data[grouped_data['Plec'] == 'M']['Liczba dzieci'], label='M', width=0.35)
    plt.xlabel('Rok')
    plt.ylabel('Liczba dzieci')
    plt.legend()

    #Seaborn
    plt.subplot(1, 2, 2)
    plt.title('Wykres w seabornie')
    sns.barplot(data=grouped_data, x='Rok', y='Liczba dzieci', hue='Plec')
    plt.xlabel('Rok')
    plt.ylabel('Liczba dzieci')

    plt.suptitle('Liczba narodzonych dzieci w latach 2010-2015', fontsize=14)

    plt.show()

Zad1()
Zad2()
Zad3()
