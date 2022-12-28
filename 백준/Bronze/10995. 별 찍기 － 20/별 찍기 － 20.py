n = int(input())
op = ['', ' ']
for i in range(n):
    print(op[i%2]+'* '*n)