from math import gcd

N = int(input())
arr = list(map(int, input().split()))
n1 = arr[0]
for i  in range(1, N):
    n2 = arr[i]
    g = gcd(n1, n2)
    print(f'{n1//g}/{n2//g}')   