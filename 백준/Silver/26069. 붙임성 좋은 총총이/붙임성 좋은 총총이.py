N = int(input())
dancer = set(['ChongChong'])
for _ in range(N):
    n1, n2 = input().split()
    if n1 in dancer or n2 in dancer:
        dancer.add(n1)
        dancer.add(n2)
print(len(dancer))