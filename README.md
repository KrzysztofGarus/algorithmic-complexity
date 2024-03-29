# algorithmic-complexity
Comparing various computational complexities

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


# linear vs exponential fibonacci
Comparing the computational complexity of two methods (linear and exponential) for creating numbers from the fibonacci sequence
```py
a = 1
b = 1
i = 0
fibs = []
# FAST FIB
def fib_good(n):
    global a
    global b
    global i
    global fibs
    if n < 0:
        print("bad input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        while(i < n / 2):
            fibs.append(a)
            fibs.append(b)
            a = a + b
            b = a + b
            i = i + 1
    return fibs
# SLOW FIB
def fib_bad(n):
    if n < 0:
        print("bad input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib_bad(n-1) + fib_bad(n-2)
from timeit import default_timer as timer
def calculate_time_good(n):
    start = timer()
    fib_good(n)
    end = timer()
    return end - start
def calculate_time_bad(n):
    start = timer()
    fib_bad(n)
    end = timer()
    return end - start
    
# good fib values
gxv = list(range(1, 10000))
gyv = []
for x in range(1, 10000):
    gyv.append(calculate_time_good(x))
    
# bad fib values
bxv = list(range(1, 36))
byv = []
for x in range(1, 36):
    byv.append(calculate_time_bad(x))
    
import matplotlib.pyplot as plt
import numpy as np


plt.plot(bxv, byv)
plt.title("Bad Fibonacci")
plt.xlabel("Length of list (number)")
plt.ylabel("Time taken (seconds)")
plt.show()

plt.plot(gxv, gyv)
plt.title("Good Fibonacci")
plt.xlabel("Length of list (number)")
plt.ylabel("Time taken (seconds)")
plt.show()


plt.plot(gxv, gyv, "-b", label="good fib")
plt.plot(bxv, byv, "-r", label="bad fib")
plt.title("Comparison")
plt.xlabel("Length of list (number)")
plt.ylabel("Time taken (seconds)")
plt.legend(loc="upper left")
plt.show()
```
![bad_fib](https://user-images.githubusercontent.com/117105005/200169869-79fff1a3-65d2-40b0-9954-81bb74e84028.png)
![good_fib](https://user-images.githubusercontent.com/117105005/200169870-c4aac18b-d8c1-488a-ab9e-d7daec090b57.png)
![comparison_fib](https://user-images.githubusercontent.com/117105005/200170575-f54528b0-c622-4378-9ed4-f2293eed4a19.png)


# Wyszkiwanie binarne

Porównanie złożoności obliczeniowej dwóch metod wyszukiwania elementu w liście - liniowego oraz binarnego


Do celów badawczych tworzymy posortowaną listę 100000 liczb z zakresu 1 do 100000
```py
import random
dataset = [random.randint(1,100000) for x in range(1,100000)]
dataset = sorted(dataset)
```

Standardowa procedura wyszukiwania liczby sprawdza wszystkie elementy listy od początku aż dojdzie do pasującej
```py
# wyszukiwanie liczby x w ciągu 100000 liczb w przedziale 1-100000
# gdy podana liczba nie występuje w ciągu - zwracamy wartość -1

def standard_find(x):
    i = 0
    index = -1
    for numbers in dataset:
        if x == dataset[i]:
            return i
        i += 1
    return index
```
Wyszukiwanie binarne działa na innej zasadzie:
- sprawadzamy czy szukany element znajduje się w pierwszej lub drugiej połowie naszej listy wyznaczając jej środek
- jeśli mamy szczęście i element znajduje się w środku listy - program zwraca pozycję szukanego elementu
- jeśli nie mamy szczęścia, to sprawdzamy czy środkowy element jest mniejszy lub większy od naszej liczby
- jeśli jest mniejszy to bierzemy pod uwagę pierwszą połowę listy a w przeciwnym wypadku drugą
- operację powtarzamy aż nie znajdziemy liczby wyznaczając kolejne środki 
- w najgorszym wypadku dojdziemy do momentu gdy nasza lista będzie posiadała tylko jeden element

```py
def binary_find(x):
    start = 0
    end = len(dataset) - 1
    mid = 0
    while (start <= end):
        mid = (start + end) // 2
        if dataset[mid] == x:
            return mid
        if dataset[mid] < x:
             start = mid + 1
             index = mid
        else:
            end = mid - 1
    return mid
```

Poniżej porównanie działania obu sposobów wyszukiwania na przykładzie wyszukiwania liczby 37

![binary-and-linear-search-animations](https://user-images.githubusercontent.com/117105005/200673713-efe3199d-058d-4389-9ca5-7986ac0d7683.gif)

Porównajmy czasy wyszukiwania - wykres przedstawia ilość czasu potrzebną do znalezienia szukanej liczby dla liczb w zakresie od 1 do 100000
Test został wykonany na kompuerze z ryzenem 5900x, 32gb ram, 2tb ssd - w przypadku wykonania testu na słabszym sprzęcie czas wyszukiwania linearnego byłby dużo większy i bardziej zauważalny dla użytkownika

![binary_linear](https://user-images.githubusercontent.com/117105005/200679487-1dd239f8-6999-49bd-8825-ea5d62841f25.png)
