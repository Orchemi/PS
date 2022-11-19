def check(txt, tl):
    s, e = 0, tl-1
    while e-s >= 1:
        if txt[s]!=txt[e]: return False
        s += 1
        e -= 1
    return True

txt = input()
l = len(txt)
i = 0
while i < l:
    new_txt = txt[i:]
    if check(new_txt, l-i): break
    i += 1

print(l+i)