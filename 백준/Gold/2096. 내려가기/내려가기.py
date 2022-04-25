import sys
input = sys.stdin.readline

N = int(input())
startlst = list(map(int, input().split()))
maxlst = startlst[::]
minlst = startlst[::]

i = 1
while i < N:
    a, b, c = map(int, input().split())
    maxL = max(maxlst[0], maxlst[1])
    maxR = max(maxlst[1], maxlst[2])
    maxC = max(maxL, maxR)
    minL = min(minlst[0], minlst[1])
    minR = min(minlst[1], minlst[2])
    minC = min(minL, minR)

    maxlst[0] = a + maxL
    maxlst[1] = b + maxC
    maxlst[2] = c + maxR
    minlst[0] = a + minL
    minlst[1] = b + minC
    minlst[2] = c + minR
    i += 1

print(max(maxlst), min(minlst))