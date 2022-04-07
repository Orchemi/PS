from collections import deque

L, S = map(int, input().split())
Ls = [0]*101
Ss = [0]*101
v = [0xffffff]*101
for _ in range(L):
    s, e = map(int, input().split())
    Ls[s] = e
for _ in range(S):
    s, e = map(int, input().split())
    Ss[s] = e

Q = deque()
Q.append(1)
v[1] = 0
cnt = 1
l = 1
while v[100]==0xffffff:
    for _ in range(l):
        n = Q.popleft()
        l -= 1

        for k in range(1, 7):
            s = n+k
            if s > 100: continue
            if v[s] <= cnt: continue
            # 밟은 자리에 뱀이 있다면
            if Ss[s]:
                if v[Ss[s]] > cnt:
                    v[Ss[s]] = cnt
                    Q.append(Ss[s])
                    l += 1
                continue

            # 탐색 위치에 cnt를 지정하고, Q에 좌표 추가
            v[s] = cnt
            Q.append(s)
            l += 1

            # 밟은 자리에 사다리가 있고, 사다리를 타고 올라간 곳의 v가 cnt보다 크다면
            if Ls[s] and v[Ls[s]] > cnt:
                # cnt를 추가하고 좌표 추가
                v[Ls[s]] = cnt
                Q.append(Ls[s])
                l += 1
    cnt += 1

print(v[100])