N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

S = 0
N2 = 0
while N:
    a = A[N2]
    b = B[N-1]
    S += a*b
    N -= 1
    N2 += 1
print(S)