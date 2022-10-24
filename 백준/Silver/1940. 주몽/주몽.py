import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
S = set(map(int, input().split()))
cnt = 0
while S:
    s = S.pop()
    if M-s in S:
        S.remove(M-s)
        cnt += 1
print(cnt)