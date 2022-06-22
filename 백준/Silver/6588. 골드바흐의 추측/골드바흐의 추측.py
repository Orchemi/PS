import sys
input = sys.stdin.readline

def check(N):
    def is_prime(n):
        for i in range(2, int(n ** (1 / 2)) + 1):
            if not n % i: return 0
        return 1

    def next_s(s):
        s += 1
        while not is_prime(s):
            s += 1
        return s

    def next_e(e):
        e -= 1
        while not is_prime(e):
            e -= 1
        return e

    s = 3
    e = N-3 if is_prime(N-3) else next_e(N-3)
    while s <= e:
        ssum = s + e
        if ssum == N: return s, e
        elif ssum > N: e = next_e(e)
        elif ssum < N: s = next_s(s)
    return 0, 0


while True:
    N = int(input())
    if not N: break
    s, e = check(N)
    ret = "Goldbach's conjecture is wrong." if not (s or e) else f'{N} = {s} + {e}'
    print(ret)