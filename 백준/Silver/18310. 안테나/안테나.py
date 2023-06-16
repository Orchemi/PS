N = int(input())
hs = sorted(list(map(int, input().split())))
print(hs[N//2-(1-N%2)])