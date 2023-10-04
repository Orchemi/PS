from math import gcd, lcm

N = int(input())
arr = list(map(int, input().split()))
M = lcm(*arr)

J = 0
for a in arr:
    J += (M//a)

K = gcd(M, J)
print(f'{M//K}/{J//K}')