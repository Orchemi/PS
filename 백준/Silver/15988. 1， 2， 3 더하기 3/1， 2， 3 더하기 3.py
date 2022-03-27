def f(n):
    global m, L
    while not m[n]:
        L += 1
        m[L] = (m[L-1]+m[L-2]+m[L-3])%M
    return m[n]

m = [0]*(10**6+1)
M = 1000000009
m[1], m[2], m[3] = 1, 2, 4
L = 3
T = int(input())
for _ in range(T):
    n = int(input())
    print(f(n))