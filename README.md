# algorithmic-complexity
Comparing various computational complexities
```py

a = 1
b = 1
i = 0
fibs = [0]

def fib(n):
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
![pobrane](https://user-images.githubusercontent.com/117105005/200167992-12896fc5-3a94-439a-94a8-1057607ca3d3.png)


```
