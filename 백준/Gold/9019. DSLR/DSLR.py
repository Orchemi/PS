import sys
input = sys.stdin.readline
from collections import deque

def check(num2, txt, char):
    global visit, Q
    if not visit[num2]:
        visit[num2] = txt+char
        Q.append((txt+char, num2))


T = int(input())
for _ in range(T):
    b, t = map(int, input().split())
    visit = ['']*10001
    Q = deque()
    Q.append(('', b))
    while not visit[t]:
        txt, num = Q.popleft()

        # D인 경우
        num2 = (num*2)%10000
        check(num2, txt, 'D')

        # S인 경우
        num2 = (num-1)%10000
        check(num2, txt, 'S')

        # L인 경우
        num2 = (num%1000)*10 + (num//1000)
        check(num2, txt, 'L')

        # R인 경우
        num2 = (num//10) + (num%10)*1000
        check(num2, txt, 'R')

    print(visit[t])