def calc_tf(n):
    def calc_k(n, k):
        cnt = 0
        while n:
            cnt += n // k
            n = n // k
        return cnt

    return calc_k(n, 2), calc_k(n, 5)

n, a = map(int, input().split())
b = n - a

n2, n5 = calc_tf(n)
a2, a5 = calc_tf(a)
b2, b5 = calc_tf(b)
r2 = n2 - a2 - b2
r5 = n5 - a5 - b5
print(min(r2, r5))
