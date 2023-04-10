txt = input()
arr0 = txt.split('::')
l0 = len(arr0)
if l0==1:
    pre_ret = arr0[0].split(':')
else:
    arr1 = arr0[0].split(':')
    arr2 = arr0[1].split(':')
    l1, l2 = len(arr1), len(arr2)
    pre_ret = [*arr1, *['' for _ in range(8-(l1+l2))], *arr2]

ret = []
for p in pre_ret:
    pl = len(p)
    ret.append('0'*(4-pl)+p)
print(':'.join(ret))