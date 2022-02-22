r1, r2 = ord('a'), ord('z')
lows = range(r1, r2+1)
S = list(map(chr, lows))

txt = input()

for char in S:
    if char in txt:
        print(txt.index(char), end=' ')
    else:
        print(-1, end=' ')