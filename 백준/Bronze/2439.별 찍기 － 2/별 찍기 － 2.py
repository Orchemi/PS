n = int(input())

for i in range(1, n+1):
    stars = '*' * i
    print(f'{stars:>{n}}')