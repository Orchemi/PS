W, H = map(int, input().split())
N = int(input())

lst_c, lst_r = [0], [0]
for _ in range(N):
    d, i = map(int, input().split())
    k = lst_c if d else lst_r
    k.append(i)

def Func(arr, N):
    arr.append(N)
    arr.sort()

    ret = 0
    i = 0

    while arr[i] != N:
        if ret < arr[i+1] - arr[i]:
            ret = arr[i+1] - arr[i]
        i += 1
    return ret

print(Func(lst_c,W) * Func(lst_r,H))