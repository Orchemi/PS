def main(std_i):
    ret = 0
    for k in range(1, std_i):
        ret += check(std_i, k)

    for k in range(std_i+1, N+1):
        ret += check(std_i, k)

    return ret

def check(std_i, k):
    dx = std_i - k
    dy = arr[std_i] - arr[k]
    s = dy/dx
    [b, e] = [k+1, std_i] if std_i > k else [std_i+1, k]

    for j in range(b, e):
        std_h = s*j + (arr[k] - s*k)
        if arr[j] >= std_h:
            return 0
    return 1


N = int(input())
arr = [0] + list(map(int, input().split()))
ret = 0
for std_i in range(1, N+1):
    ret = max(ret, main(std_i))

print(ret)