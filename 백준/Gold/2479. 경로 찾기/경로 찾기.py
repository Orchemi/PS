import sys
input = sys.stdin.readline
from collections import deque

T, L = map(int, input().split())
arr = []
for _ in range(T):
    arr.append(int(input()[::-1], 2))

mat = []
for i in range(T):
    num = 0
    for j in range(T):
        cnt = 0
        for k in range(L):
            if (arr[i]^arr[j]) & (1<<k):
                cnt += 1
                if cnt==2:
                    cnt = 0
                    break
        num += (1<<j)*cnt
    mat.append(num)

for i in range(L):
    mat[i] &= ~(1<<i)

S, E = map(int, input().split())
S, E = S-1, E-1

paths = deque()
paths.append([S])
Q = deque()
Q.append(S)
v = 0
while not v & (1<<E) and Q:
    s = Q.popleft()
    path = paths.popleft()
    for i in range(T):
        if v&(1<<i): continue
        if not mat[s]&(1<<i): continue
        v ^= (1<<i)
        if i==E:
            path += [i]
            for n in path:
                print(n+1, end=' ')
            quit()
        Q.append(i)
        paths.append(path+[i])
print(-1)