from collections import deque

Q = deque(list(input()))
cnt = 0
txt = ''
while Q:
    t = Q.popleft()
    txt += t
    cnt += 1
    if cnt==10:
        cnt = 0
        print(txt)
        txt = ''
if txt: print(txt)