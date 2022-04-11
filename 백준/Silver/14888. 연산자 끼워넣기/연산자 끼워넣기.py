def foo(i, ret):
    global ops

    if i==N:
        global minV, maxV
        minV = min(minV, ret)
        maxV = max(maxV, ret)
        return

    for k in range(4):
        if not ops[k]: continue
        ops[k] -= 1

        if not k: foo(i+1, ret+arr[i])
        elif k==1: foo(i+1, ret-arr[i])
        elif k==2: foo(i+1, ret*arr[i])
        else:
            if ret < 0:
                foo(i+1, -(-ret//arr[i]))
            else:
                foo(i+1, ret//arr[i])

        ops[k] += 1

N = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
minV = 0xfffffff
maxV = -0xfffffff
foo(1, arr[0])

print(maxV)
print(minV)