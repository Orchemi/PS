import sys
input = sys.stdin.readline

N = int(input())
Q = []
Q += list(map(int, input().split()))
for _ in range(N-1):
    Q += list(map(int, input().split()))
    Q.sort(reverse=True)
    for _ in range(N):
        Q.pop()

print(Q[N-1])