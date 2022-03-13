N = int(input())
for _ in range(N):
    txt = input()
    l = 0
    for t in txt:
        if t=='(':
            l += 1
        else:
            if l:
                l -= 1
            else:
                l = 1
                break
    print('NO' if l else 'YES')