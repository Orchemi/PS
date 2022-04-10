N = int(input())
X = 3 if N<3 else N+1
f = [0]*X
f[0], f[1], f[2] = 1, 1, 2

now = 3
while now <= N:
    f[now] = (f[now-1]+f[now-2]) % 15746
    now += 1

print(f[N] % 15746)