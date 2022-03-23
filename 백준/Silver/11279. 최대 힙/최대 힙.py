import sys
input = sys.stdin.readline

def enq(n):
    global last, arr
    last += 1
    arr[last] = n
    c = last
    p = last//2

    while p and arr[p] < arr[c]:
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = c//2
    

def deq():
    global last, arr
    tmp = arr[1]
    arr[1] = arr[last]
    last -= 1

    p = 1
    c = 2
    while c <= last:
        if c+1 <= last and arr[c] < arr[c+1]:
            c += 1

        if arr[c] > arr[p]:
            arr[c], arr[p] = arr[p], arr[c]
            p = c
            c = 2*p
        else:
            break

    print(tmp)


N = int(input())
last = 0
arr = [0]*100002

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