import sys
input = sys.stdin.readline

def main():
    def place_sharks():
        sharks = {}
        for m in range(M):
            i, j, s, d, z = map(int, input().split())
            mat[i-1][j-1].append((z, s, d, m))
            sharks[m] = (i-1, j-1, z, s, d)
        return sharks

    def hunt_shark():
        size = 0
        for i in range(I):
            if not mat[i][kj]: continue
            z, s, d, m = mat[i][kj].pop()
            sharks[m] = ()
            sharks_nums.remove(m)
            size = z
            break
        return size

    def move_sharks():
        new_sharks = {}
        for m in sharks_nums:
            i, j, z, s, d = sharks[m]
            mat[i][j].pop()
            ni, nj, nd = move_shark(i, j, s, d)
            new_sharks[m] = (ni, nj, z, s, nd)
        return new_sharks

    def move_shark(i, j, s, d):
        if not s:
            return i, j, d

        di, dj = DD[d]
        if di:
            return move_vertical(i, j, s, d)
        else:
            return move_horizontal(i, j, s, d)

    def move_vertical(i, j, s, d):
        di, dj = DD[d]
        s = s%((I-1)*2)
        while True:
            si = i+di*s
            if 0<=si<I: return si, j, d
            move_i = I-1-i if di > 0 else i
            i = i+move_i if di > 0 else i-move_i
            s -= move_i
            di *= -1
            d = RD[d]

    def move_horizontal(i, j, s, d):
        di, dj = DD[d]
        s = s%((J-1)*2)
        while True:
            sj = j+dj*s
            if 0<=sj<J: return i, sj, d
            move_j = J-1-j if dj > 0 else j
            j = j+move_j if dj > 0 else j-move_j
            s -= move_j
            dj *= -1
            d = RD[d]

    def fill_sharks():
        for m in sharks_nums:
            i, j, z, s, d = sharks[m]
            if not mat[i][j]:
                mat[i][j].append((z, s, d, m))

            else:
                if mat[i][j][0][0] > z:
                    remove_sharks_set.add(m)
                else:
                    rm = mat[i][j][0][3]
                    remove_sharks_set.add(rm)
                    mat[i][j].pop()
                    mat[i][j].append((z, s, d, m))

    def remove_sharks():
        for rm in remove_sharks_set:
            remove_shark(rm)
        remove_sharks_set.clear()

    def remove_shark(m):
        sharks_nums.remove(m)
        sharks[m] = ()


    I, J, M = map(int, input().split())
    mat = [[[] for _ in range(J)] for _ in range(I)]
    sharks = place_sharks()
    sharks_nums = set(range(M))
    remove_sharks_set = set()

    RD = {1:2, 2:1, 3:4, 4:3}
    DD = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}

    ret = 0
    for kj in range(J):
        ret += hunt_shark()
        sharks = move_sharks()
        fill_sharks()
        remove_sharks()
    return ret

print(main())