arr = [0]*26
txt = input()
for t in txt:
    arr[ord(t)-97] += 1

print(*arr)