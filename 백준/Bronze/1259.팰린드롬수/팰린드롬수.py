def func(n):
    if len(n) < 2:
        print('yes')
    elif n[0] == n[-1]:
        return func(n[1:-1])
    else:
        print('no')

while True:
    n = input()
    if n == '0':
        break
    func(n)