import sys
input = sys.stdin.readline

def is_prime(M):
    if M <= 10:
        return base_primes[M]
    for i in range(2, int(M ** (1 / 2)) + 1):
        if not M % i: return 0
    return 1

def next_prime(M):
    while not is_prime(M):
        M += 1
    return M

def make_primes(M):
    l = 0
    arr = [1] * M
    primes = []
    for i in range(2, int(M ** (1 / 2)) + 1):
        if arr[i]:
            l += 1
            primes.append(i)
            for j in range(i * 2, M, i):
                arr[j] = 0

    for i in range(int(M ** (1 / 2)) + 1, M):
        if arr[i]:
            l += 1
            primes.append(i)

    return primes, l

base_primes = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0 ,0]
M = int(input())
primes, l = make_primes(M)

primes.append(next_prime(M))
l += 1

accs = [0]
for p in primes:
    accs.append(accs[-1]+p)

def main(N):
    s, e = 0, 1
    cnt = 0
    while e <= l:
        if s >= e:
            e += 1
            continue

        diff = accs[e] - accs[s]
        # 누적합이 N보다 작은 경우
        if diff < N:
            e += 1

        # 누적합이 N보다 큰 경우
        elif diff > N:
            s += 1

        # 누적합이 N인 경우
        else:
            cnt += 1
            e += 1
            s += 1
    return cnt

cnt = main(M)
if is_prime(M) and primes and primes[-1] < M:
    cnt += 1
print(cnt)