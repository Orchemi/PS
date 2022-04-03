from collections import deque

def Rotate():
    global status, CV
    CV.appendleft(CV.pop())
    k = N-1
    while k > 0:
        status[k] = status[k-1]
        k -= 1
    status[0] = status[N-1] = 0

def Move(i):
    global status, CV
    k = i
    while k > 0:
        if status[k-1] and not status[k] and CV[k]:
            status[k], status[k-1] = 1, 0
            checkHurt(k)
            CV[k] -= 1
        k -= 1

def Insert():
    global status, CV
    if not CV[0]: return
    status[0] = 1
    checkHurt(0)
    CV[0] -= 1


def checkHurt(i):
    if CV[i]==1:
        global hurt
        hurt += 1

N, K = map(int, input().split())
CV = deque(list(map(int, input().split())))
status = deque([0]*N)

cnt = 0
hurt = 0
while hurt < K:
    Rotate()
    Move(N-1)
    status[N-1] = 0
    Insert()
    cnt += 1

print(cnt)