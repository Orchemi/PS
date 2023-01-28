import sys
input = sys.stdin.readline

def main():
    def find_heights():
        H = [set() for _ in range(501)]
        for i in range(I):
            for j in range(J):
                H[mat[i][j]].add((i, j))
        return H

    def check_around(i, j, h):
        if not (i, j) in H[mat[i][j]]: return
        H[mat[i][j]].remove((i, j))

        for di in range(-1, 2):
            si = i+di
            if not 0<=si<I: continue
            for dj in range(-1, 2):
                sj = j+dj
                if not 0<=sj<J: continue
                if mat[si][sj] > h: continue
                check_around(si, sj, mat[si][sj])
        return
        
    
    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    H = find_heights()
    cnt = 0
    while H:
        if not H[-1]:
            H.pop()
            continue
            
        while H[-1]:
            i, j = H[-1].pop()
            H[-1].add((i, j))
            check_around(i, j, mat[i][j])
            cnt += 1
    return cnt

print(main())          