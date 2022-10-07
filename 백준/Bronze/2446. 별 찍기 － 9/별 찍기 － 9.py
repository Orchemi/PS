N = int(input())
blank = 0
cnt = N*2-1
while True:
    print(f'{" "*blank}{"*"*cnt}')
    blank += 1
    cnt -= 2
    if cnt == -1:
        blank -= 2
        cnt += 4
        break

while cnt <= N*2-1:
    print(f'{" " * blank}{"*" * cnt}')
    blank -= 1
    cnt += 2