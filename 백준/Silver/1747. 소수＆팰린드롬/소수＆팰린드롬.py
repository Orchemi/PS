def isPal(x):
    x2 = ''.join(reversed(list(str(x))))
    return str(x)==x2

N = 1004000
v = [1]*N
v[1] = 0
for i in range(2, N):
    if v[i]:
        for j in range(i+i, N, i):
            v[j] = 0

k = int(input())
while True:
    if v[k] and isPal(k): break
    k += 1

print(k)