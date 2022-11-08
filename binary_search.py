import random
from timeit import default_timer as timer
  
dataset = [random.randint(1,10000) for x in range(1,10000)]
dataset = sorted(dataset)

def standard_find(x):
    i = 0
    index = -1
    for numbers in dataset:
        if x == dataset[i]:
            return i
        i += 1
    return index
  
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
  
def calculate_time_binary_find(n):
    start = timer()
    binary_find(n)
    end = timer()
    return end - start
  
def calculate_time_standard_find(n):
    start = timer()
    standard_find(n)
    end = timer()
    return end - start
  
# good find values
gxv = list(range(1, 100000))
gyv = []
for x in range(1, 100000):
    gyv.append(calculate_time_binary_find(x))
    
# bad find values

bxv = list(range(1, 100000))
byv = []
for x in range(1, 100000):
    byv.append(calculate_time_standard_find(x))
    
import matplotlib.pyplot as plt
import numpy as np


plt.plot(gxv, gyv, "-b", label="binary")
plt.plot(bxv, byv, "-r", label="linear")
plt.title("Comparison")
plt.xlabel("Length of list (number)")
plt.ylabel("Time taken (seconds)")
plt.legend(loc="upper left")
plt.show()
