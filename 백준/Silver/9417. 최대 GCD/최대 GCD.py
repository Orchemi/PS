import sys
input = sys.stdin.readline
from math import gcd

def main():
    maxx = 0
    arr = list(map(int, input().split()))
    al = len(arr)
    for i in range(al-1):
        n1 = arr[i]
        for j in range(i+1, al):
            n2 = arr[j]
            maxx = max(maxx, gcd(n1, n2))
    return maxx

T = int(input())
for _ in range(T):
    print(main())