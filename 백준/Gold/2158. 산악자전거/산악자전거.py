import sys
input = sys.stdin.readline
from collections import deque

V, I, J = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(I)]
time = [[float('inf')]*J for _ in range(I)]
time[0][0] = 0

Q = deque()
Q.append((0, 0, V))
while Q:
    ni, nj, speed = Q.popleft()
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        si, sj = ni+di, nj+dj
        if not (0<=si<I and 0<=sj<J): continue
        if time[si][sj] <= time[ni][nj] + (1/speed): continue
        time[si][sj] = time[ni][nj] + (1/speed)
        speed_new = speed * (2**(mat[ni][nj]-mat[si][sj]))
        Q.append((si, sj, speed_new))

print(f'{time[I-1][J-1]:.2f}')