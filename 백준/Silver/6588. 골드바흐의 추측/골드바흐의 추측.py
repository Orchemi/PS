import sys
input = sys.stdin.readline

def find_primes():
    check_list = [1]*K
    primes = []

    for m in range(4, K, 2):
        check_list[m] = 0

    for n in range(3, K):
        if not check_list[n]: continue
        primes.append(n)
        for m in range(n*2, K, n):
            check_list[m] = 0
    return primes, check_list

def main():
    for p in primes:
        if p*2 > N: break
        if check_list[N-p]: return f'{N} = {p} + {N-p}'
    return "Goldbach's conjecture is wrong."

K = 1000001
primes, check_list = find_primes()
while True:
    N = int(input())
    if not N: break
    print(main())