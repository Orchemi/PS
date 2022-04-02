import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dictA = {}

for a in arr:
    dictA[a] = dictA.get(a, 0) + 1

sumV = 0
dictB = {}
for k in sorted(list(dictA.keys())):
    dictB[k] = sumV
    sumV += 1

for a in arr:
    print(dictB[a], end=' ')