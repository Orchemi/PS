import sys
input = sys.stdin.readline

n = 123456
v = [1]*(n*2+1)
for i in range(2, n*2+1):
    if v[i]:
        for j in range(i+i, n*2+1, i):
            v[j] = 0

v2 = [0]*(n*2+1)
for i in range(1, n*2+1):
    v2[i] = v2[i-1]+v[i]

while True:
    N = int(input())
    if not N: break
    print(v2[N*2]-v2[N])