import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ret = 0
    a = 1
    while a < n:
        a2 = a**2
        b = a+1
        while b < n:
            tmp = (a2+b**2+m)/(a*b)
            if tmp==int(tmp): ret += 1
            b += 1
        a += 1
    print(ret)