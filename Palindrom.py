# Palindrom to coś, co czyta się tak samo od przodu i od tyłu.
#  Hipoteza: weź dowolną liczbę naturalną. Jeżeli nie jest palindromem,
# to zapisz ją od tyłu i dodaj obie liczby. Jeżeli wynik nadal nie jest palindromem, kontynuuj, traktując go jako daną. Przerwij, gdy osiągniesz palindrom. Na przykład: 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884. Napisz program sprawdzający hipotezę dla pierwszych 200 liczb naturalnych jako startowych. Czy zawsze osiągniemy palindrom?

# funkcja zwracająca palindrom
def szukaj_palindromu(num):
    sum = 0
    sum += int(num)

    # pętla działa tak długo, kiedy sum rzutowane na string nie jest taka sama jak string od tyłu
    while str(sum) != str(sum)[::-1]:
        # przypisanie zmiennej next_num sumy od tyłu
        next_num = int(str(sum)[::-1])
        # sumowanie obu liczb
        sum += next_num
    return sum

# pętla sprawdzająca palindromy dla liczb 0 - 200
for i in range(1, 201):
    # program wpadnie w nieskończoną pętlę przy 200 i 196. Dla tych liczb nie można osiągnąć palindromu
    if(i != 196 and i != 200):
        print('Palindrom dla {}:'.format(i), szukaj_palindromu(i))
    else:
        print('Nie istnieje palindrom dla {}'.format(i))

print('Koniec Programu')

# Przykładowy wynik programu:
# Palindrom dla 175: 9559
# Palindrom dla 176: 44044
# Palindrom dla 177: 8836886388
# Palindrom dla 178: 15851
# Palindrom dla 179: 1661
# Palindrom dla 180: 747
# Palindrom dla 181: 181
# Palindrom dla 182: 45254
# Palindrom dla 183: 13431
# Palindrom dla 184: 2552
# Palindrom dla 185: 4774
# Palindrom dla 186: 6996
# Palindrom dla 187: 8813200023188
# Palindrom dla 188: 233332
# Palindrom dla 189: 1881
# Palindrom dla 190: 45254
# Palindrom dla 191: 191
# Palindrom dla 192: 6996
# Palindrom dla 193: 233332
# Palindrom dla 194: 2992
# Palindrom dla 195: 9339
# Nie istnieje palindrom dla 196
# Palindrom dla 197: 881188
# Palindrom dla 198: 79497
# Palindrom dla 199: 3113
# Nie istnieje palindrom dla 200
# Koniec Programu