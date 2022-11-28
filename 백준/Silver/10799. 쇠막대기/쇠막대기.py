txt = input()
ret, l = 0, 0
for i in range(len(txt)):
    if txt[i]=='(':
        l+=1
        continue

    l -= 1
    p = l if txt[i-1]=='(' else 1
    ret += p

print(ret)