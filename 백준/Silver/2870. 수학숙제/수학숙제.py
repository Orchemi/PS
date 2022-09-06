def main():
    global ret
    txt = input()
    check = True
    for t in txt:
        if t.isnumeric():
            if check: ret.append('0')
            ret[-1]+=t
            check = False
        else:
            check=True

N = int(input())
ret = []
for _ in range(N):
    main()

ans = sorted(list(map(int, ret)))
for a in ans:
    print(a)