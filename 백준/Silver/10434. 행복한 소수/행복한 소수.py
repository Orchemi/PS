def main(N):
    def is_prime(N):
        for n in range(2, int(N**(1/2))+1):
            if not N%n: return False
        return True

    if N==1: return 'NO'
    if not is_prime(N):
        return 'NO'

    N = str(N)
    visit = {N}
    while True:
        N = str(sum([int(n)**2 for n in N]))
        if N=='1': return 'YES'
        if N in visit: return 'NO'
        visit.add(N)

for _ in range(int(input())):
    t, N = map(int, input().split())
    print(t, N, main(N))