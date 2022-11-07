def prime_test(a):
    if a == 1:
        return True
    if a == 2:
        return True
    for i in range(2, a // 2):
        if a % i == 0:
            return False
    return True
    
print(prime_test(11))

count = 0
for i in range(1, 1000):
    if prime_test(i):
        count += 1
        
print(count)