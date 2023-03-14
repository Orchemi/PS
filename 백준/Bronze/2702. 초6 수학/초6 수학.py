from math import lcm, gcd

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))