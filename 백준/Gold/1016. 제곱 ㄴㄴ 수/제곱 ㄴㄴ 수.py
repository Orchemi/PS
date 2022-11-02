mn, mx = map(int, input().split())
check = [1]*(mx-mn+1)

sqr_n = 2
while sqr_n**2 <= mx:
    sqr_nn = sqr_n**2
    k = (mx//sqr_nn)*sqr_nn
    while k >=mn:
        check[k-mn] = 0
        k -= sqr_nn
    sqr_n += 1

print(sum(check))