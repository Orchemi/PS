def main():
    def make_S():
        S = {}
        cur_words = words[:]
        for word in cur_words:
            i = 0
            word_list = list(word)
            while word_list:
                w = word_list.pop()
                S[w] = S.get(w, 0) + 10**i
                i += 1
        return S

    def match():
        lst = sorted(S.values())
        ret, n = 0, 9
        while lst:
            ret += n * lst.pop()
            n -= 1
        return ret

    N = int(input())
    words = [input() for _ in range(N)]
    S = make_S()
    return match()

print(main())