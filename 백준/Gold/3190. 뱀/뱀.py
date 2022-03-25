from collections import deque

def Play():
    global mat, arr
    hi, hj, hd = 0, 0, 0
    mat[hi][hj] = 1
    Q = deque()
    Q.append((hi, hj))

    time = 0
    for t, d in arr:
        while time < t:
            forward = headSee(hi, hj, hd)
            if forward==-1: return time + 1
            si, sj = forward
            fowInfo = mat[si][sj]
            mat[si][sj] = 1
            Q.append((si, sj))
            hi, hj = si, sj

            if not fowInfo:
                li, lj = Q.popleft()
                mat[li][lj] = 0

            time += 1
        td = -1 if d=='L' else 1
        hd += td
        if not 0<=hd<4:
            hd %= 4


def headSee(i, j, d):
    di, dj = dd[d]
    si, sj = i+di, j+dj
    if not (0<=si<N and 0<=sj<N): return -1
    if mat[si][sj]==1: return -1
    return si, sj

N = int(input())
mat = [[0]*N for _ in range(N)]
AN = int(input())
for _ in range(AN):
    i, j = map(int, input().split())
    mat[i-1][j-1] = 4

L = int(input())
arr = []
for _ in range(L):
    t, d = input().split()
    arr.append((int(t), d))
arr.append((10000,''))

dd = [(0,1), (1,0), (0,-1), (-1,0)]
print(Play())