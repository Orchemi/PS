cnt = int(input())
ls = []

for i in range(cnt):
    A, B = input().split()
    C = int(A) + int(B)
    ls.append(C)

for C in ls:
    print(C)