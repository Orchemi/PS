def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if not n%i: return False
    return True

def main():
    N = int(input())
    if N < 2: return 2
    while not is_prime(N):
        N += 1
    return N

T = int(input())
for _ in range(T):
    print(main())