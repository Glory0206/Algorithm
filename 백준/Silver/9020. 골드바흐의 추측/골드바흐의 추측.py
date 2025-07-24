import sys
import math

T = int(sys.stdin.readline())

def is_prime(x):
    if x == 2:
        return True
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for _ in range(T):
    n = int(sys.stdin.readline())

    for i in range(n//2, 1, -1):
        if is_prime(i) and is_prime(n-i):
            print(i, n-i)

            break
