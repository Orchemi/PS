while True:
    k = input()
    if k=='0 0 0':
        break
    a, b, c = map(int, k.split())
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b

    if (a**2)+(b**2)==(c**2):
        print('right')
    else:
        print('wrong')