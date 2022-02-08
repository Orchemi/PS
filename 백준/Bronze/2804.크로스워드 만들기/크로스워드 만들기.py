A, B = input().split()

for i in A:
    if i in B:
        a = A.index(i)
        b = B.index(i)
        break

flag = 0
for idx, val in enumerate(B):

    if val == B[b] and flag == 0:
        result = A
        flag = 1
    else:
        lst = ['.']*len(A)
        lst[a] = B[idx]
        result = ''.join(lst)

    print(result)