ls = []

for i in range(10):
    a = int(input())
    ls.append(a)

ls2 = [i % 42 for i in ls]
set1 = set(ls2)
print(len(set1))
