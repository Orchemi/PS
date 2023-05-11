def reverse(str): return int(str[::-1])
arrs = list(input().split())
arrs.pop(0)

while True:
    try:
        lst = list(input().split())
        arrs += lst
    except:
        break

ret = sorted([reverse(str) for str in arrs])
print(*ret, sep='\n')