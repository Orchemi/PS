def main():
    N = int(input())
    nums = list(map(int, input().split()))
    ND = [0]*53
    for n in nums:
        ND[n] += 1

    RD = [0]*53
    txt = input()
    for t in txt:
        if t==' ':
            RD[0] += 1
            continue

        if t.islower():
            n = ord(t) - 70
        else:
            n = ord(t) - 64
        RD[n] += 1

    for n in range(53):
        if RD[n] != ND[n]: return 'n'
    return 'y'

print(main())