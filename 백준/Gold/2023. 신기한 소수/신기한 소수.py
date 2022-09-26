def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if not n%i: return False
    return True

N = int(input())
now = 1
primes = [2, 3, 5, 7]
while now < N:
    new_primes = []
    for prime in primes:
        for i in range(1, 10):
            p = prime*10+i
            if is_prime(p):
                new_primes.append(p)
    primes = new_primes
    now += 1

for p in primes:
    print(p)