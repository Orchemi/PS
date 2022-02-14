X = int(input())
i = 1

while X > i:
    X -= i
    i += 1

if i % 2:
    r = (i+1) - X
    c = X
else:
    r = X
    c = (i+1) - r

print(f'{r}/{c}')