# Liczby Armstronga to N-cyfrowa liczba naturalna która jest sumą
# swoich cyfr podniesionych do potęgi N. Na przykład: 153 = 13+53+33.
# Proszę napisac program znajdujący jak najwięcej takich liczb..

for i in range(1, 10000):
    num_length = len(str(i)) #określenie długości cyfry (od tego zależy potęga)
    power = int(num_length) #potęga to długość cyfry
    digit_sum = 0 #ustawienie sumy cyfr na 0
    num = i  #num to liczba, na której obecnie pracujemy
    while num > 0: #zapobiegnięcie wejścia w infinite loop poprzez wyodrębnienie cyfry
      digit = num % 10 #użycie modulo zwróci ostatnią cyfrę numeru, na którym pracujemy
      digit_sum += pow(digit, power) #podnieś do potęgi i dodaj do sumy
      num //= 10

    if i == digit_sum:
      print(i) #jeżeli jest to liczba Armstronga, wydrukuj na ekranie

print('Koniec programu')

#przykładowy wynik programu
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474
#Koniec programu