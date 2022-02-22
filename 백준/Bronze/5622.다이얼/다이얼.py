tele = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

txt = input()
txt_lst = [char for char in txt]

result = 0
for char in txt_lst:
    for idx, alphas in enumerate(tele):
        if char in alphas:
            result += idx + 3
            break

print(result)