import sys
input = sys.stdin.readline

def enq(n):
    global last, arr
    last += 1
    arr[last] = n
    c = last
    p = last//2

    while p and arr[c] < arr[p]:
        arr[c], arr[p] = arr[p], arr[c]
        c = p
        p = c//2

def deq():
    global last, arr
    ret = arr[1]
    arr[1] = arr[last]
    last -= 1

    p = 1
    c = 2
    while c <= last:
        if c+1 <= last and arr[c+1] < arr[c]:
            c += 1

        if arr[c] < arr[p]:
            arr[c], arr[p] = arr[p], arr[c]
            p = c
            c = p*2

        else:
            break

    print(ret)


arr = [0]*100001
last = 0
N = int(input())
for _ in range(N):
    n = int(input())

    if n:
        enq(n)
    else:
        if last > 0:
            deq()
        else:
            print(0)
            continue