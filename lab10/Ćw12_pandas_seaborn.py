import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


"""
Przypomnienie bibliteki Pandas i Matplotlib oraz wprowadzenie do biblioteki Seaborn
"""


def file_importer():
    df_zamowienia = pd.read_csv('./zamowienia.csv', sep=';')
    return df_zamowienia


def sortowanie1(df):
    """Sortowanie"""
    # krok 1 - dane należy posortować chronologicznie
    # jeżeli chcemy nadpisać ramkę ramką posortowaną:
    df1 = df.sort_values(by=['Data zamowienia'])
    # przy zwykłym wyświetleniu (i nie nadpisaniu danych w dataframe):
    print(df.sort_values(by=['Data zamowienia']))
    # parametr ascending pozwala na określenie kierunku sortowania, w liście możemy określić kolejne kolumny, po których chcemy sortować

    # aby nadpisać ramkę używamy trybu inplace oraz dodatkowo, jeżeli jest to postać docelowa, ignorujemy indeks w operacji sortowania
    df_copy_2 = df.copy(deep=True)
    df_copy_2.sort_values(by=['Data zamowienia'], inplace=True, ignore_index=True)  # użycie inplace nadpisuje dataframe !!!!
    print(df_copy_2.head())
    # proszę zwrócić uwagę na numery indeksów i porównać do bloku powyżej


def sortowanie2(df, display_header=True):
    """Inny sposób na resetowanie indeksu"""
    # index można jednak "zresetować" również poza operacją sortowania
    # najpierw nieuporządkowana postać
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    df.sort_values(by=['Data zamowienia'], inplace=True)
    if display_header:
        print(df.head())

    # reset indeksu
    df.reset_index(drop=True, inplace=True)
    if display_header:
        print(df.head())


def przyrost_pandas(df):
    """Przyrost wartości zamówień w czasie"""
    # przyrost wartości zamówień możemy osiągnąć poprzez użycie sumy skumulowanej,
    # więc dla wiarygodności danych niezbędne było nam posortowanie danych wg.daty
    # (ze resetowanym indeksem)
    sortowanie2(df, False)
    print(df['Utarg'].cumsum().head())
    df['Utarg'].cumsum().plot()
    """
    Nie wygląda to najlepiej i niewiele z tego wykresu wynika. 
    Powodem jest wartość, którą zwróciła poprzednia operacja a jest nią pandas Series 
    gdzie mamy indeks w postaci indeksu kolejnej wartości sumy skumulowanej,
    więc nie mamy do dyspozycji kolumny z datą.
    """

    # możemy utworzyć pomocniczą serię danych z indeksem w postaci daty
    df[['Data zamowienia', 'Utarg']].set_index('Data zamowienia').cumsum().plot()
    plt.show()


def przyrost_seaborn(df):
    # użycie biblioteki seaborn
    sortowanie2(df, False)
    sns.lineplot(data=df, x='Data zamowienia', y=np.cumsum(df['Utarg']))
    plt.show()


"""
Uruchomienie kodu poniżej:
"""


def main():
    przyrost_pandas(file_importer())
    # przyrost_seaborn(file_importer())


if __name__ == "__main__":
    main()
