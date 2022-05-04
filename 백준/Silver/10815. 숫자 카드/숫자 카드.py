import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dic = {}
for a in arr:
    dic[a] = 1

M = int(input())
arr2 = list(map(int, input().split()))
for a in arr2:
    print(dic.get(a, 0), end=' ')