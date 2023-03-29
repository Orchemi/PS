N = int(input())
for _ in range(N):
    n, txt = input().split()
    n = int(n)
    txt = list(txt)
    
    txt.pop(n-1)
    print(''.join(txt))