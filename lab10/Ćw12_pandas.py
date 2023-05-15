import pandas as pd


"""
Przypomnienie elementów biblioteki Pandas:
"""


def file_importer():
    df_zamowienia = pd.read_csv('./zamowienia.csv', sep=';')
    return df_zamowienia


def blok1(df):
    print(df.head())  # aby pokazać wynik df.head(), musimy użyć funkcji print()


def blok2(df):
    print(df.describe())
    print(df['Utarg'].describe())


def blok3(df):
    df.info()  # funkcja nie potrzebuje wyświetlenia printem
    """Z uzyskanych informacji wynika, że pandas nie wykonał automatycznej konwersji wartości 
    w kolumnie Data zamowienia na typ datetime. Należy to zrobić ręcznie.
    """
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    print()
    df.info()


def blok4(df):
    df.info()
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'], format='%Y-%m-%d')
    print()
    df.info()
    print(df.head())


def blok5(df):
    df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
    df['year'] = df['Data zamowienia'].dt.year
    df['month'] = df['Data zamowienia'].dt.month
    df['day'] = df['Data zamowienia'].dt.day
    print(df.head())
    print(pd.to_datetime(df[['year', 'month', 'day']]))
    df.drop(columns=['year', 'month', 'day'], inplace=True)
    print()
    df.info()


def blok6(df):
    """W porównaniu do tego samego fragmentu w Jupyterze, nie musimy tworzyć kopii zbioru,
    ponieważ w tym skrypcie (.py) za każdym razem wywołujemy funkcję file_importer(), która ładuje
    nowy df. Stąd niektóre kroki są pomijane (np. nie musimy konwertować kolumny z powrotem na str)
    """
    df['rok'] = df['Data zamowienia'].str[:4]
    df['Nowa data'] = df['Data zamowienia'].str.replace('-', '/')
    print(df.head())


def blok7(df):
    df['Jeszcze nowsza data'] = df['Data zamowienia'].apply(str.replace, args=('-', '/'))
    print(df.head())


"""
Uruchomienie kodu poniżej:
"""


def main():
    blok1(file_importer())


if __name__ == "__main__":
    main()
