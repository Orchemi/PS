import sys
input = sys.stdin.readline
from collections import deque

def main():
    txt = input().rstrip()
    N = int(input())

    content = input().rstrip().strip('[').strip(']')
    Q = deque(content.split(',')) if content else deque()

    opp = 0
    for t in txt:
        # 함수가 R이면 방향 바꿈
        if t == 'R':
            opp ^= 1
            continue

        # 함수가 D인데 Q가 없으면 error
        if not Q: return 'error'

        # 정방향이면 popleft 역방향이면 pop
        Q.pop() if opp else Q.popleft()

    # 역방향이라면 Q를 역순으로 배치
    if opp: Q.reverse()
    
    return f"[{','.join(Q)}]"


T = int(input())
for _ in range(T):
    print(main())