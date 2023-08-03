def main():
    def find_winner(j):
        a, b = mat[0][j], mat[1][j]
        if a==b: return ''
        if a == 1: return 'a' if b==3 else 'b'
        if a == 2: return 'a' if b==1 else 'b'
        if a == 3: return 'a' if b==2 else 'b'

    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(2)]
    cur_win = ''
    A_wins = [0]
    B_wins = [0]
    for j in range(N):
        cur_ret = find_winner(j)
        if not cur_ret:
            if cur_win == 'a':
                A_wins.append(0)
                B_wins[-1] += 1
                cur_win = 'b'
            else:
                B_wins.append(0)
                A_wins[-1] += 1
                cur_win = 'a'
        elif cur_ret == 'a':
            A_wins[-1] += 1
            B_wins.append(0)
            cur_win = 'a'
        else:
            B_wins[-1] += 1
            A_wins.append(0)
            cur_win = 'b'

    return max([max(A_wins), max(B_wins)])

print(main())