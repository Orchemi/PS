def main():
    a, b = input().split()
    ps = a.split(b)
    ret = len(ps)-1
    for p in ps:
        ret += len(p)
    return ret


T = int(input())
for _ in range(T):
    print(main())