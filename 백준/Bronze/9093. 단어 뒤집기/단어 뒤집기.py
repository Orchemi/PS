def main():
    arr = list(input().split())
    for a in arr:
        print(rev(a), end=' ')
    print()

def rev(txt):
    return ''.join(list(txt)[::-1])

T = int(input())
for _ in range(T):
    main()