def main():
    N = input()
    ret, i = 1, 0
    while True:
        for s in str(ret):
            if N[i]==s: i += 1
            if i == len(N): return ret
        ret += 1

print(main())