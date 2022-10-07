import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    name, *scores = input().split()
    scores = [int(i) for i in scores]
    arr.append((name, *scores))

arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for a in arr:
    print(a[0])