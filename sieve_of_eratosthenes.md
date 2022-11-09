# Sito Eratostenesa

Sito Eratostenesa jest algorytmem, który szybko znajduje wszystkie liczby pierwsze z przedziału [2...n]

Algorytm polega na odsiewaniu wielokrotności kolejnych liczb

Na początku mamy zbiór wszystkich liczb naturalnych od 2 do n.
W każdym kroku wybieramy najmniejszą, nierozpatrzoną liczbę, po czym wykreślamy wszystkie jej wielokrotności. Należy pamiętać, że każda liczba złożona ma dzielnik mniejszy bądź równy pierwiastkowi z tej liczby. Reasumując wystarczy wykreślać tylko wielokrotności liczb pierwszych mniejszych od pierwiastka z n.

Poniżej graficzne przedstawienie działania sita

![Sieve_of_Eratosthenes](https://user-images.githubusercontent.com/117105005/200827157-bddbd6cc-cd19-4070-9c5a-a670f484640c.gif)

Czas na implementację sita w pythonie.
Poniższy kod zwraca liczby pierwsze do końca podanego zakresu - n

```py
import math

# funkcja sita

def erat2(n): 
    imax = int(math.sqrt(n))+1    
    primes = [True]*(n+1)
    for i in range(2,imax+1):
         if primes[i]: 
            for j in range(i+i,n+1,i): 
                primes[j] = False 
    result = [] 
    for i in range(2,n+1): 
         if primes[i]: result.append(i) 
    return result
```

Poniżej funkcja sprawdzacjąca, czy dana liczba jest pierwsza. Sprawdza czy dana liczba jest podzielna przez wszystkie liczby z zakresu 2 do połowy liczby
```py
def prime_test(a):
    if a == 1:
        return True
    if a == 2:
        return True
    for i in range(2, a // 2):
        if a % i == 0:
            return False
    return True
```

Aby porównać czas działania obu algorytmów musiałem dodać pętlę, która uruchamia algorytm dla wszystkich liczb z zakresu 2 do n

```py
def calculate_time_prime_test(n):
    start = timer()
    for a in range(2, n):
        prime_test(a)
    end = timer()
    return end - start
```
Wyniki porównania przedstawiają się następująco

![sito](https://user-images.githubusercontent.com/117105005/200861342-8348e0aa-f9a8-45c1-98d6-b505cb794f87.png)

Przykładowo dla sprawdzenia liczb z zakresu 2..10000 sito potrzebuje niecałą milisekundę natomiast zwykły test potrzebuje około 140 razy więcej czasu :D
Ktoś może pomyśleć, że to spora różnica... a co powiesz na to, że dla zakresu 2..100000 sito potrzebuje 10 ms czyli proporcjonalnie 10 razy dłużej niż wcześniej a zwykły test 10.5 sekundy? To już jest ponad 1000 razy wolniej :(

W takim razie chyba już ustaliliśmy co wybierzesz następnym razem do wyszukiwania liczb pierwszych ;)

![choose](https://user-images.githubusercontent.com/117105005/200867019-40617537-1618-4cae-86ff-24b3228d2c88.jpg)


