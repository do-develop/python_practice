import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

   
# eratosthenes sieve
num = 1000
array = [True for i in range(num + 1)] # consider all numbers are prime first

for i in range(2, int(math.sqrt(num)) + 1):
    if array[i] == True:
        j = 2
        while i*j <= num:
            array[i * j] = False
            j += 1


        
        
