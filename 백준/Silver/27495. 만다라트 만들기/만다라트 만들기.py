def find_centers():
    around_M = [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0)]
    arounds = sorted([(mat[3*ri+1][3*rj+1], (3*ri+1, 3*rj+1)) for ri, rj in around_M])
    return arounds

def find_arounds(ci, cj):
    around_D = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    return sorted([mat[ci+di][cj+dj] for di, dj in around_D])

mat = [list(input().split()) for _ in range(9)]
centers = find_centers()
for M in range(8):
    center_txt, center_pos = centers[M]
    ci, cj = center_pos
    print(f'#{M+1}. {center_txt}')

    arounds = find_arounds(ci, cj)
    for i in range(8):
        print(f'#{M+1}-{i+1}. {arounds[i]}')