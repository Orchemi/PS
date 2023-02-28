import sys
input = sys.stdin.readline

def main():
    def make_memo():
        memo = [[0]*J for _ in range(I)]
        memo[0][0] = mat[0][0]
        for j in range(1, J):
            memo[0][j] = memo[0][j-1]+mat[0][j]
        for i in range(1, I):
            memo[i][0] = memo[i-1][0]+mat[i][0]
        for i in range(1, I):
            for j in range(1, J):
                memo[i][j] = memo[i-1][j]+memo[i][j-1]-memo[i-1][j-1]+mat[i][j]
        return memo


    I, J = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(I)]
    memo = make_memo()
    T = int(input())
    for _ in range(T):
        i1, j1, i2, j2 = map(lambda x: int(x)-1, input().split())
        a = memo[i1-1][j2] if i1 else 0
        b = memo[i2][j1-1] if j1 else 0
        c = 0 if not (i1 and j1) else memo[i1-1][j1-1]
        print(memo[i2][j2]-a-b+c)

main()