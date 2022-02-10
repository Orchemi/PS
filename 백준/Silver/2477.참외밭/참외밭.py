N = int(input())
lst1 = []
lst2 = []

for i in range(6):
    d, l = map(int, input().split())
    lst1.append(d)
    lst2.append(l)

lst1.extend(lst1)
lst2.extend(lst2)

for i in range(8):
    if (lst1[i]==lst1[i+2]) and (lst1[i+1]==lst1[i+3]):
        a1 = lst2[i] + lst2[i+2]
        a2 = lst2[i+1] + lst2[i+3]
        b1 = lst2[i+2]
        b2 = lst2[i+1]
        break

S = a1*a2 - b1*b2

print(N*S)