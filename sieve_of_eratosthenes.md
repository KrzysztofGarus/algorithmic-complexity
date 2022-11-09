# Sito Eratostenesa

Sito Eratostenesa jest algorytmem, który szybko znajduje wszystkie liczby pierwsze z przedziału [2...n]

Algorytm polega na odsiewaniu wielokrotności kolejnych liczb

Na początku mamy zbiór wszystkich liczb naturalnych od 2 do n.
W każdym kroku wybieramy najmniejszą, nierozpatrzoną liczbę, po czym wykreślamy wszystkie jej wielokrotności. Należy pamiętać, że każda liczba złożona ma dzielnik mniejszy bądź równy pierwiastkowi z tej liczby. Reasumując wystarczy wykreślać tylko wielokrotności liczb pierwszych mniejszych od pierwiastka z n.

Poniżej graficzne przedstawienie działania sita

![Sieve_of_Eratosthenes](https://user-images.githubusercontent.com/117105005/200827157-bddbd6cc-cd19-4070-9c5a-a670f484640c.gif)

Czas na implementację sita w pythonie:

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
