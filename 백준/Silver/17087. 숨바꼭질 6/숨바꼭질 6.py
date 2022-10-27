from math import gcd

N, S = map(int, input().split())
arr = list(map(lambda x: (abs(int(x)-S)), input().split()))
print(gcd(*arr))