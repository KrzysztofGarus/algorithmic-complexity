# Wyszkiwanie binarne

Porównanie złożoności obliczeniowej dwóch metod wyszukiwania elementu w liście - liniowego oraz binarnego


Do celów badawczych tworzymy posortowaną listę 100000 liczb z zakresu 1 do 100000
```py
import random
dataset = [random.randint(1,100000) for x in range(1,100000)]
dataset = sorted(dataset)
```
