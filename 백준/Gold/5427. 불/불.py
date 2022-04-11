from collections import deque

def findsang():
    global mat
    for i in range(I):
        for j in range(J):
            if mat[i][j]=='@':
                return i, j
            
def main():
    # 불 좌표 확인
    fires = deque()
    fl = 0
    for i in range(I):
        for j in range(J):
            if mat[i][j] == '*':
                fires.append((i, j))
                fl += 1

    # 상근 좌표 확인
    ni, nj = findsang()
    sangmoves = deque()
    sangmoves.append((ni, nj))
    ml = 1

    # visit
    firevisit = [[0]*J for _ in range(I)]
    for fi, fj in fires:
        firevisit[fi][fj] = 1
    sangvisit = [[0]*J for _ in range(I)]
    sangvisit[ni][nj] = 1

    time = 1
    while sangmoves:
        # 불 이동
        for _ in range(fl):
            fi, fj = fires.popleft()
            fl -= 1

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                sfi, sfj = fi+di, fj+dj
                if not (0<=sfi<I and 0<=sfj<J): continue
                if firevisit[sfi][sfj]: continue
                if mat[sfi][sfj] == '#': continue
                firevisit[sfi][sfj] = 1
                fires.append((sfi, sfj))
                fl += 1

        # 상근 이동
        for _ in range(ml):
            ni, nj = sangmoves.popleft()
            ml -= 1

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                si, sj = ni+di, nj+dj
                if not (0<=si<I and 0<=sj<J): return time
                if firevisit[si][sj]: continue
                if sangvisit[si][sj]: continue
                if mat[si][sj]=='#': continue
                sangvisit[si][sj] = 1
                sangmoves.append((si, sj))
                ml += 1
        time += 1

    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    J, I = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    print(main())