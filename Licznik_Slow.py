# Proszę napisad program, który wczytuje tekst z podanego pliku i wypisuje 20 najczęściej występujących w nim słów. Program powinien ignorowad krótkie słowa (krótsze niż 5 liter) typu: i, lub, się, aby, żeby , itp. Proszę podad wyniki dla tekstu „Pana Tadeusza”.

# funkcja usuwająca znaki specjalne z tekstu
def usun_znaki_specjalne(tekst):
    nowy_tekst = tekst

    nowy_tekst = nowy_tekst.replace(':', '')
    nowy_tekst = nowy_tekst.replace('.', '')
    nowy_tekst = nowy_tekst.replace(';', '')
    nowy_tekst = nowy_tekst.replace(',', '')
    nowy_tekst = nowy_tekst.replace('?', '')
    nowy_tekst = nowy_tekst.replace('!', '')
    nowy_tekst = nowy_tekst.replace('«', '')
    nowy_tekst = nowy_tekst.replace('»', '')
    nowy_tekst = nowy_tekst.replace('…', '')
    nowy_tekst = nowy_tekst.replace('(', '')
    nowy_tekst = nowy_tekst.replace(')', '')
    nowy_tekst = nowy_tekst.replace('*', '')

    return nowy_tekst

def analizuj_tekst(nazwa_pliku):
    f = open(nazwa_pliku, 'r', encoding='utf-8-sig')
    # stworzenie słownika przechowywującego słowa i liczbę ich powtórzeń
    zbior_slow = {}
    # zmienna przechowująca tekst
    tekst = f.read()
    f.close()
    # usunięcie przecinków, kropek etc z tekstu
    tekst = usun_znaki_specjalne(tekst)
    # rozdzielenie słów w pliku (tworzy tablicę stringów)
    tablica_slow = tekst.split()

    for slowo in tablica_slow:
        # sprawdzenie czy słowo jest dłuższe niż 5
        if len(slowo) > 4:
            # sprawdzenie, czy istnieje już klucz będący danym słowem
            if (slowo.lower() not in zbior_slow):
                # jeśli nie istnieje, tworzymy klucz będący słowem i przypisujemy początkową wartość 1
                zbior_slow[slowo.lower()] = 1
            else:
                # jeśli istnieje, inkrementujemy o 1
                zbior_slow[slowo.lower()] += 1
    
    return zbior_slow

# funkcja sortująca słowa po liczbie ich wystąpień w tekście
def pokaz_top20(slownik):
    # sortowanie elementów w słowniku od najczęściej występujących do najrzadziej
    posortowane_slowa = sorted(slownik, key=lambda x: slownik[x], reverse=True)
    # wypisanie pierwszych 20 najczęstszych słów
    counter = 0
    print('Najczęściej występujące słowa to:')
    for k in posortowane_slowa:
        if counter < 20:
            print("{} : {}".format(k, slownik[k]))
            counter += 1
    
slowa = analizuj_tekst('pan-tadeusz.txt')
pokaz_top20(slowa)

# Rezultat programu:
# Najczęściej występujące słowa to:
# rzekł : 155
# tylko : 149
# hrabia : 129
# sędzia : 127
# tadeusz : 106
# przed : 102
# jeszcze : 101
# przez : 97
# gdzie : 94
# wszyscy : 90
# wojski : 89
# potem : 86
# teraz : 83
# niech : 76
# kiedy : 74
# jeśli : 73
# który : 72
# nawet : 71
# znowu : 71
# wszystko : 67