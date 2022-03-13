import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
P1, P2 = map(int, input().split())
P1, P2 = P1-1, P2-1
E = int(input())
link = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    link[a].append(b)
    link[b].append(a)

# BFS 시작
visited = [0]*N
Q = [(P1, 0)]
start = -1
end = 1

while start < end-1:
    start += 1
    per, chon = Q[start]

    if not visited[per]:
        visited[per] = 1

        if per==P2:
            print(chon)
            quit()

        lst = [(i, chon+1) for i in link[per]]
        Q.extend(lst)
        end += len(lst)

print(-1)
