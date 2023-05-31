def main():
    def find_words(lst, l):
        word = ''
        for i in range(l):
            if lst[i]=='#':
                if len(word)>1:
                    words.append(word)
                word = ''
            else:
                word += lst[i]
        if len(word) > 1:
            words.append(word)

    I, J = map(int, input().split())
    mat = [list(input()) for _ in range(I)]

    words = []
    for lst in mat:
        find_words(lst, J)

    for j in range(J):
        lst = [mat[i][j] for i in range(I)]
        find_words(lst, I)

    return sorted(words)[0]

print(main())