ds = input()
ret = 10
state = ds[0]
for i in range(1, len(ds)):
    if ds[i] == state:
        ret += 5
    else:
        ret += 10
        state = ds[i]

print(ret)