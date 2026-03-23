
from math import ceil, factorial

def float_ceil_factorial(n):
    if n < 0:
        return -1
    else:
        ceil_value = ceil(n)
        return factorial(ceil_value)
    
n = float(input())

output = float_ceil_factorial(n)

print(output)
        



