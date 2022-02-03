idx = 1
max_idx = 0
max_val = 0

for i in range(5):
    score = sum(list(map(int, input().split())))

    if max_val < score:
        max_val = score
        max_idx = idx
    idx += 1

print(max_idx, max_val)