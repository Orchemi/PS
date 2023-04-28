type, txt = input().split()
if type == '1' or type == '3':
    origin = ['']
    for t in txt:
        if t.isupper():
            origin.append(t.lower())
        else:
            origin[-1] += t

    if not origin[0]: origin.pop(0)

elif type == '2':
    origin = txt.split('_')

pascal = ''
for p in origin:
    pascal += p[0].upper() + p[1:]
camel = pascal[0].lower() + pascal[1:]
snake = '_'.join(origin)

print(camel)
print(snake)
print(pascal)