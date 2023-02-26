def main():
    def dfs(bi, acc):
        if bi > l: return 0, 0
        i = bi
        ret = 0
        while i < l:
            if S[i] == ')': return i, ret
            if S[i] == '(':
                ret -= acc
                ei, accv = dfs(i+1, acc*int(S[i-1]))
                i = ei+1
                ret += accv
            else:
                ret += acc
                i += 1
        return i, ret

    S = input()
    l = len(S)
    ei, ret = dfs(0, 1)
    return ret

print(main())