from math import lcm
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))