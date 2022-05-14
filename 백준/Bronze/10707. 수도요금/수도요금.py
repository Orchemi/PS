A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

C1 = A*P
C2 = B
if P >= C:
    C2 += (P-C)*D

print(min(C1, C2))