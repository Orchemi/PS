N = int(input())

if N == 1:
    quit()

n = 2
while N >= n:
    if N % n == 0:
        N /= n
        print(n)
        n -= 1

    n += 1