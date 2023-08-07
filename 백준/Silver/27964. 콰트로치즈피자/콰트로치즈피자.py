def main():
    N = int(input())
    chs = set(list(input().split()))
    cnt = 0
    for ch in chs:
        if ch[-6:] == 'Cheese':
            cnt += 1
    return 'yummy' if cnt >= 4 else 'sad'

print(main())