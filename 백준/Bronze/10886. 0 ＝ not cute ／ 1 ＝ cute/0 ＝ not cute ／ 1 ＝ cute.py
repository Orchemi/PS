T = int(input())
cnt = sum([int(input()) for _ in range(T)])
op = cnt*2 < T
print(f'Junhee is {"not " if op else ""}cute!')