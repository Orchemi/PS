tcs = int(input())
out_cnt = 0

for tc in range(tcs):
    txt = input()
    out_lst = []

    char_now = txt[0]
    len1 = 0
    for char in txt:

        if char in out_lst:
            out_cnt += 1
            break

        if char_now == char:
            continue
        else:
            out_lst.append(char_now)
            char_now = char

print(tcs - out_cnt)