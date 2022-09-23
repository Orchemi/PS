import sys
from itertools import permutations

n = int(input())
k = int(input())
arr = [input() for _ in range(n)]

S = set()
for perm in permutations(arr, k):
    ret = ''
    for i in range(k):
        ret += perm[i]
    S.add(ret)

print(len(S))