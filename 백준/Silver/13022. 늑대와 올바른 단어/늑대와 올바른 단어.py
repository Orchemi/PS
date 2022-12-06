def main():
    def check_main():
        pl = check_len_per_part(i)
        if i+pl*4 > tl: return False
        for j in range(1, 4):
            if check_per_part(i+pl*j, pl, list('wolf')[j]): continue
            return False
        return pl*4

    def check_len_per_part(ii):
        pl = 0
        while ii < tl and txt[ii]=='w':
            pl += 1
            ii += 1
        return pl

    def check_per_part(si, pl, c):
        for pi in range(pl):
            if txt[si+pi] == c: continue
            return False
        return True

    txt = input()
    if txt[0] != 'w': return 0
    tl = len(txt)
    i = 0
    while i < tl:
        check_ret = check_main()
        if not check_ret: return 0
        i += check_ret
    return 1

print(main())