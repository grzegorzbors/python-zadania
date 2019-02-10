# Komputer jest doskonałym narzędziem służącym do szyfrowania i deszyfrowania tajnych wiadomości. W metodzie Gronsfelda, będącą modyfikacją szyfru Cezara, stosuje się klucz liczbowy. Biorąc klucz o wartości 31206 i niezaszyfrowany tekst „PROGRAMOWANIE”, uzyskujemy następujący szyfrogram: 31206 31206 312 PROGR AMOWA NIE SSQGX DNQWG QJG Kolejne litery są przesuwane o kolejne wartości z klucza. Proszę napisad programy dokonujące szyfrowania i deszyfrowania pliku tekstowego zadanym kluczem.

def szyfr_groensfelda(klucz, nazwa_pliku, akcja):
    wyjsciowy_tekst = ''
    tekst = czytaj_plik(nazwa_pliku)
    alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #rozbicie tekstu na tablicę słów
    tablica_slow = tekst.upper().split()
    dlugosc_klucza = len(str(klucz))
    #rozbicie klucza na tablicę składowych cyfr
    tablica_klucz = [int(c) for c in str(klucz)]
    dlugosc_alfabetu = len(alfabet)
    
    #iteracja przez każde słowo w tekście
    for slowo in tablica_slow:
        #zmienna przechowująca długość słowa
        dlugosc_slowa = len(slowo)
        #zmienna przechowująca nowe słowo
        nowe_slowo = ''
        #ustawienie licznika długości klucza
        licznik = 0
            
        #iteracja po literach słowa
        for litera in slowo:
            #znalezienie indeksu litery w alfabecie
            indeks_litery = alfabet.index(litera)
            #konkatenacja podmienionych liter do slowa
            #flaga 'szyfruj' w wywołaniu funkcji informuje, że odbywa się akcja szyfrowania
            if akcja == 'szyfruj':
                indeks_zastapienia = indeks_litery + tablica_klucz[licznik]
            else:
                indeks_zastapienia = indeks_litery - tablica_klucz[licznik]
            #jesli indeks zastapienia nie wykracza poza indeks tablicy, to zastąp bezpośrednio, bo nie wykroczy poza granicę tablicy
            if dlugosc_alfabetu > indeks_zastapienia:
                nowe_slowo += alfabet[indeks_zastapienia]
            #jesli indeks zastapienia wykracza poza indeks tablicy
            else:
                #odjęcie od większego indeksu długości alfabetu - w ten sposób uzyskujemy indeks liczony o dodatkowe indeksy, które były poza granicą, od początku
                indeks_poza = indeks_zastapienia - dlugosc_alfabetu
                nowe_slowo += alfabet[indeks_poza]
            #inkrementacja licznika, jeśli klucz jest dłuższy niż 2
            licznik += 1
            #jeśli słowo jest dłuższe od klucza i licznik wykracza poza indeks klucza, ustaw licznik na 0 (wtedy liczenie po indeksach klucza zacznie się od nowa)
            if (dlugosc_klucza < dlugosc_slowa) and (licznik > dlugosc_klucza - 1):
                licznik = 0

        #konkatenacja zaszyfrowanego słowa pełnym tekstem, który będzie zwracać funkcja
        #nie dodawaj spacji, jeśli to początek tekstu
        if wyjsciowy_tekst == '':
            wyjsciowy_tekst += nowe_slowo
        else:
            wyjsciowy_tekst += (" " + nowe_slowo)

    #jeśli flaga to 'szyfruj', zapisz plik z zaszyfrowanym tekstem
    if akcja == 'szyfruj':
        zapisz_plik(wyjsciowy_tekst, 'ZaszyfrowanyTekst')
    else:
        zapisz_plik(wyjsciowy_tekst, 'OdszyfrowanyTekst')

    return wyjsciowy_tekst

#funkcja wczytująca dany plik .txt i zwraca jego zawartość
def czytaj_plik(nazwa_pliku):
    p = open(nazwa_pliku,"r")
    tekst = p.read()
    p.close()
    return tekst

#funkcja zapisująca plik z rezultatem szyfrowania
def zapisz_plik(tekst, nazwa_pliku):
    p = open(nazwa_pliku+'.txt', "w")
    p.write(tekst)
    p.close()

#wywołanie funkcji szyfrowania (trzeci parametr w funkcji to flaga determinująca czy szyfrowanie lub odszyfrowanie)
szyfr_groensfelda(31206, 'DoZaszyfrowania.txt', 'szyfruj')
#DoZaszyfrowania.txt zawiera tekst 'programowanie jest super'
#rezultatem jest zapisany plik 'ZaszyfrowanyTekst.txt'
#zawartość: SSQGXDNQWGQJG MFUT VVREX

#wywołanie funkcji odszyfrowania
szyfr_groensfelda(31206, 'ZaszyfrowanyTekst.txt', 'odszyfruj')
#'ZaszyfrowanyTekst.txt' zawiera tekst 'SSQGXDNQWGQJG MFUT VVREX'
#rezultatem wywołania jest nowo powstały plik tekstowy OdszyfrowanyTekst.txt z zawartością:
#PROGRAMOWANIE JEST SUPER