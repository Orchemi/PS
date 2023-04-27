def main():
    txt = input()
    s, e = 0, len(txt)-1
    while e-s >= 1:
        if txt[s]!=txt[e]: return 0
        s, e = s+1, e-1
    return 1

print(main())