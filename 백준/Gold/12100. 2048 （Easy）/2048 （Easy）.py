def shift_line(arr):
    global N
    def find_initial_blank(arr):
        global N
        i = 0
        while i < N:
            if arr[i]: i += 1
            else: return i
        return N

    def pull_nums(j, ni, arr):
        global N
        while j < N:
            if arr[j]:
                arr[ni] = arr[j]
                arr[j] = 0
                ni += 1
            j += 1
        return arr

    def combine(arr):
        global N
        j = 1
        while j < N:
            if arr[j] == arr[j-1]:
                arr[j] = 0
                arr[j-1] *= 2
                j += 1
            j += 1
        return arr

    j = ni = find_initial_blank(arr)
    arr = pull_nums(j, ni, arr)
    arr = combine(arr)
    j = ni = find_initial_blank(arr)
    return pull_nums(j, ni, arr)


def DFS(mat, depth):
    global N, total_max
    if depth == 5:
        cur_max = 0
        for i in range(N):
            for j in range(N):
                if cur_max < mat[i][j]:
                    cur_max = mat[i][j]
        total_max = max(total_max, cur_max)
        return

    DFS(LEFT([line[:] for line in mat]), depth+1)
    DFS(RIGHT([line[:] for line in mat]), depth+1)
    DFS(UP([line[:] for line in mat]), depth+1)
    DFS(DOWN([line[:] for line in mat]), depth+1)


def LEFT(mat):
    global N
    for i in range(N):
        mat[i] = shift_line(mat[i])
    return mat

def RIGHT(mat):
    global N
    for i in range(N):
        mat[i] = shift_line(mat[i][::-1])[::-1]
    return mat

def UP(mat):
    global N
    new_mat = [[0]*N for _ in range(N)]
    for j in range(N):
        arr = []
        for i in range(N):
            arr.append(mat[i][j])
        arr = shift_line(arr)
        for i in range(N):
            new_mat[i][j] = arr[i]
    return new_mat

def DOWN(mat):
    global N
    new_mat = [[0]*N for _ in range(N)]
    for j in range(N):
        arr = []
        for i in range(N):
            arr = [mat[i][j]] + arr
        arr = shift_line(arr)
        for i in range(N):
            new_mat[i][j] = arr.pop()
    return new_mat


N = int(input())
mat_origin = [list(map(int, input().split())) for _ in range(N)]
mat = [line[:] for line in mat_origin]

total_max = 0
DFS(mat, 0)
print(total_max)