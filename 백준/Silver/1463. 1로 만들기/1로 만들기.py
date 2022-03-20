N = int(input())
arr = [-1]*(N+1)
arr[N] = 0

Q = [N]
front = -1
while arr[1]==-1:
    front += 1
    K = Q[front]
    k = arr[K]+1

    if not K%3 and arr[K//3]==-1:
        arr[K//3] = k
        Q.append(K//3)

    if not K%2 and arr[K//2]==-1:
        arr[K//2] = k
        Q.append(K//2)

    if (K > 0) and arr[K-1]==-1:
        arr[K-1] = k
        Q.append(K-1)

print(arr[1])