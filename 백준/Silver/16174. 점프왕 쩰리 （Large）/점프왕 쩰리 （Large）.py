def main():
    global Q, mat
    while Q:
        ci, cj = Q.pop()
        if not mat[ci][cj]: continue
        if jump(ci+mat[ci][cj], cj): return True
        if jump(ci, cj+mat[ci][cj]): return True
    return False


def jump(i, j):
    global Q, N, ans, mat
    if i>=N or j>=N: return False
    if i==j==N-1: return True
    Q.add((i, j))


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
Q = set()
Q.add((0, 0))
print('HaruHaru' if main() else 'Hing')