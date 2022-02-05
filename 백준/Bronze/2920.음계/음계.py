put = list(map(int, input().split()))

a = put[0] - put[1]
n = 2

while n < 8:
    if put[n-1]-put[n] != a:
        print('mixed')
        quit()

    n += 1

if a == -1:
    print('ascending')
elif a == 1:
    print('descending')