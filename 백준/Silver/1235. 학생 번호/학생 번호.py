T = input()
arr = [input() for _ in range(int(T))]
s = len(T)-1
l = len(arr[0])
for n in range(s, l+1):
    arr2 = set([char[l-1-n:l] for char in arr])
    if len(arr2) == int(T): break
print(n+1)