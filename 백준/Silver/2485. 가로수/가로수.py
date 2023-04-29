import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
trees = sorted([int(input()) for _ in range(N)])

diffs = [trees[i+1]-trees[i] for i in range(N-1)]
print((trees[-1]-trees[0])//gcd(*diffs)-1-(N-2))