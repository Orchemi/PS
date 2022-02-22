txt = input().upper()

txt_lst = [char for char in txt]

dict1 = {}

for char in txt_lst:
    dict1[char] = dict1.get(char, 0) + 1

max_val = max(dict1.values())

if list(dict1.values()).count(max_val) > 1:
    print('?')
else:
    for key, val in dict1.items():
        if val != max_val:
            continue
        else:
            print(key)
            break