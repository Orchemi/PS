from collections import deque

N = int(input())
visit = [0]*(N+1)
Q = deque()
Q.append((N, [N]))
while True:
    k, path = Q.popleft()
    if k == 1: break
    if visit[k]: continue
    visit[k] = 1

    if not k%3 and not visit[k//3]:
        Q.append((k//3, path+[k//3]))

    if not k%2 and not visit[k//2]:
        Q.append((k//2, path+[k//2]))

    if 0 < k-1 and not visit[k-1]:
        Q.append((k-1, path+[k-1]))

print(len(path)-1)
print(*path)