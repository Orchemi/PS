def main():
    txt = input()
    maxx, cur = 1, 1
    prev = ''
    for t in txt:
        if t==prev:
            cur += 1
            continue

        maxx = max(maxx, cur)
        prev, cur = t, 1
    maxx = max(maxx, cur)
    print(maxx)

for _ in range(3):
    main()