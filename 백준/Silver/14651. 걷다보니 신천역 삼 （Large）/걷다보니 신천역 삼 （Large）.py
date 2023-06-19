def main():
    N = int(input())
    M = 1e9+9
    if N < 2: return 0

    ret = 2
    while N-2:
        N -= 1
        ret = (ret*3)%M
    return int(ret)

print(main())