# algorithmic-complexity
Comparing various computational complexities
```py

a = 1
b = 1
i = 0
fibs = []

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
    
from timeit import default_timer as timer

def calculate_time(n):
    start = timer()
    fib_good(n)
    end = timer()
    return end - start
    
# good fib values
xv = list(range(1, 10000))
yv = []
for x in range(1, 10000):
    yv.append(calculate_time(x))
    
    
import matplotlib.pyplot as plt
import numpy as np

plt.plot(xv, yv)
plt.show()
![pobrane](https://user-images.githubusercontent.com/117105005/200168081-236ecdc2-4989-4bfc-87b9-dac833b15102.png)

```
