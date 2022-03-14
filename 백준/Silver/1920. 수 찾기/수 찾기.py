import sys
input = sys.stdin.readline

dictA = {}

N = int(input())
nums1 = list(map(int, input().split()))
for n in nums1:
    dictA[n] = dictA.get(n, 0) + 1

M = int(input())
nums2 = list(map(int, input().split()))
for n in nums2:
    print(1 if dictA.get(n, 0) else 0)