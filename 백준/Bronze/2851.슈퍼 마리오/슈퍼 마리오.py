scores = []

for _ in range(10):
    scores.append(int(input()))

sum_val = scores[0]
cnt = 1
while (sum_val < 100) and (cnt <= 9):
    sum_val += scores[cnt]
    cnt += 1

if sum_val <= 100:
    print(sum_val)
else:
    A = sum_val - scores[cnt-1]
    B = sum_val

    if 100-A >= B-100:
        print(B)
    else:
        print(A)