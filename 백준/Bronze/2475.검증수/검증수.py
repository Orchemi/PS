import sys

lst = [i**2 for i in map(int, sys.stdin.readline().split())]
print(sum(lst) % 10)