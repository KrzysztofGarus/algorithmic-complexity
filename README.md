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

```

![good_fib](https://user-images.githubusercontent.com/117105005/200168907-c99d131e-e656-4d5a-9a50-9ecc74f1a019.png)
![bad_fib](https://user-images.githubusercontent.com/117105005/200168965-51d218cb-16fe-47f4-be36-d9995b3b257f.png)

