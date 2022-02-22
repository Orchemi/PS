a = input()
b = input()
c = input()

[A, B, C] = list(map(int, [a, b, c]))

txt = str(A*B*C)

for n in range(10):
    print(txt.count(str(n)))
