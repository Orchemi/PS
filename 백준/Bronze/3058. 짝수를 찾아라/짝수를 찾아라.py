def main():
    arr = list(map(int, input().split()))
    ret = []
    for a in arr:
        if a%2: continue
        ret.append(a)

    return sum(ret), min(ret)


T = int(input())
for _ in range(T):
    print(*main())