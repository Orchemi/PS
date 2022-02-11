lst = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
txt = input()

for char in lst:
    txt = txt.replace(char, ',')

print(len(txt))