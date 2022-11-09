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
