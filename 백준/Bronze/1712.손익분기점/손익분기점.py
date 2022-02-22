A, B, C = map(int, input().split())

if B >= C:
    result = -1
else:
    result = (A//(C-B))+1

print(result)