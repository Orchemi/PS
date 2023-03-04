from collections import deque

def main():
    def find_begin():
        for i in range(I):
            for j in range(J):
                if mat[i][j] =='0': return i, j

    def check_visits(visits, i, j):
        return visits | (2**(i*I+j))

    def check_has_key(C, keys):
        return keys & (2**(ord(C)-65))

    def register_key(c, keys):
        return keys | (2**(ord(c)-97))

    def bfs():
        Q = deque([(bi, bj, 0, 0, 0)])
        while Q:
            i, j, keys, visits, moves = Q.popleft()
            if keys in visit[i][j]: continue
            checked_visits = check_visits(visits, i, j)
            visit[i][j].add(keys)
            for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                si, sj = i+di, j+dj
                if not (0<=si<I and 0<=sj<J): continue
                if mat[si][sj] =='0':
                    Q.append((si, sj, keys, checked_visits, moves+1))
                elif mat[si][sj] == '1': return moves+1
                elif mat[si][sj] == '#': continue
                elif mat[si][sj] == '.':
                    Q.append((si, sj, keys, checked_visits, moves+1))
                else:
                    if mat[si][sj].isupper():
                        if not check_has_key(mat[si][sj], keys): continue
                        Q.append((si, sj, keys, checked_visits, moves+1))
                    else:
                        new_keys = register_key(mat[si][sj], keys)
                        Q.append((si, sj, new_keys, checked_visits, moves+1))

        return -1

    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    bi, bj = find_begin()
    visit = [[set() for _ in range(J)] for _ in range(I)]
    return bfs()

print(main())