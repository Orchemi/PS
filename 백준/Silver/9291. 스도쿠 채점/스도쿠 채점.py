def main():
    def check_list(lst):
        S = set()
        for a in lst:
            if a in S: return False
            S.add(a)
        return True

    mat = [list(map(int, input().split())) for _ in range(9)]

    # 행 체크
    for lst in mat:
        if not check_list(lst): return 'INCORRECT'

    # 열 체크
    for j in range(9):
        lst = [mat[i][j] for i in range(9)]
        if not check_list(lst): return 'INCORRECT'

    # 작은 사각형 체크
    for ki in range(0, 9, 3):
        for kj in range(0, 9, 3):
            lst = []
            for i in range(ki, ki+3):
                for j in range(kj, kj+3):
                    lst.append(mat[i][j])
            if not check_list(lst): return 'INCORRECT'
    return 'CORRECT'



T = int(input())
for t in range(1,T+1):
    print(f'Case {t}: {main()}')
    if t != T: E = input()