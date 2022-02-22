n, strd = map(int, input().split())
num_ls = map(int, input().split())
result = ''

for i in range(n):
    for num in num_ls:
        if num < strd:
            result += str(num) + ' '

print(result[:-1])