# algorithmic-complexity
Comparing the computational complexity of two methods for creating numbers from the fibonacci sequence
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
```
![bad_fib](https://user-images.githubusercontent.com/117105005/200169869-79fff1a3-65d2-40b0-9954-81bb74e84028.png)
![good_fib](https://user-images.githubusercontent.com/117105005/200169870-c4aac18b-d8c1-488a-ab9e-d7daec090b57.png)

