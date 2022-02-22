cnt = cnt_max = 0
num_init = num_max = 0

while cnt < 9:
    a = int(input())

    if num_max < a:
        num_max = a
        cnt_max = cnt

    cnt += 1

print(f'{num_max}\n{cnt_max+1}')