H, M1 = map(int, input().split())
M2 = int(input())

T = H*60 + M1 + M2
if T >= 24*60:
    T -= 24*60

H, M = T//60, T%60
print(H, M)