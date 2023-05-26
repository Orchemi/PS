import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = sorted([float(input()) for _ in range(N)])[K:N-K]
ssum = sum(scores)
s, e = scores[0], scores[-1]
print(f'{ssum/(N-2*K)+(1e-10):.2f}')
print(f'{(ssum+K*(s+e))/N+(1e-10):.2f}')