txt = input()
check = txt[0]
cnt = 1
for t in txt:
    if t==check: continue
    check = t
    cnt += 1

print(cnt//2)