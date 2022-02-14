def constructor(N):
    sum_v = N

    while N % 10 != 0:
        sum_v += (N%10)
        N //= 10
    return sum_v

N = int(input())
a = 1
while a < N:
    if N == constructor(a):
        print(a)
        quit()
    a += 1

print(0)