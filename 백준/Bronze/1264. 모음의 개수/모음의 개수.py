def main(txt):
    s1 = set('aeiou')
    s2 = set('AEIOU')
    S = s1|s2
    cnt = 0
    for t in txt:
        if t in S: cnt += 1
    print(cnt)


while True:
    txt = input()
    if txt == '#': break
    main(txt)