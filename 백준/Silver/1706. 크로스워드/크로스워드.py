def main():
    def find_words():
        words = set()
        for i in range(I):
            lst = mat[i]
            cur_words = find_words_line(lst)
            words = words | cur_words

        for j in range(J):
            lst = []
            for i in range(I):
                lst.append(mat[i][j])
            cur_words = find_words_line(lst)
            words = words | cur_words

        return words

    def find_words_line(lst):
        words = set()
        tmp = ''
        for c in lst:
            if c=='#':
                if len(tmp)>1: words.add(tmp)
                tmp = ''

            else:
                tmp += c

        if len(tmp)>1: words.add(tmp)
        return words


    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]
    words = find_words()
    return sorted(list(words))[0]

print(main())