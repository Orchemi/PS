import sys
input = sys.stdin.readline

def power():
    global S, N, T, L, M
    if S == 'N':
        S = 'N^1'

    a, b = S.split('^')
    if a == 'N':
        a = N
        b = int(b)
    elif b == 'N':
        a = int(a)
        b = N

    time = M*L/T
    return a**b <= time

def fact():
    global S, N, T, L, M

    time = M * L / T
    while N:
        time /= N
        if time < 1: return 0
        N -= 1
    return 1


C = int(input())
M = 10 ** 8
for _ in range(C):
    S, *last = input().split()
    S = S.lstrip('O(').rstrip(')')
    N, T, L = map(int, last)
    if S == 'N!':
        ret = 'May Pass.' if fact() else 'TLE!'
    else:
        ret = 'May Pass.' if power() else 'TLE!'
    print(ret)