def main():
    def check_vertical(j, c):
        for i in range(5):
            if mat[i][j] != c: return False
        return True

    def check_square(nj):
        num = ''
        for i in range(5):
            for j in range(3):
                num += mat[i][nj+j]
        return nums[num]

    N = int(input())
    I, J = 5, N//5
    string = input()
    mat = [list(string[J*i:J*(i+1)]) for i in range(5)]
    nums = {
        '####.##.##.####': '0',
        '###..#####..###': '2',
        '###..####..####': '3',
        '#.##.####..#..#': '4',
        '####..###..####': '5',
        '####..####.####': '6',
        '###..#..#..#..#': '7',
        '####.#####.####': '8',
        '####.####..####': '9',
    }

    ret = ''
    j = 0
    while j < J:
        if mat[0][j] == '.':
            j += 1
            continue

        if check_vertical(j, '#'):
            if j == J-1:
                ret += '1'
                return ret

            if check_vertical(j+1, '.'):
                ret += '1'
                j += 1
                continue

        ret += check_square(j)
        j += 3

    return ret

print(main())