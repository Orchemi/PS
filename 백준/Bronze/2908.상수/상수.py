a, b = input().split()
A, B = int(a[::-1]), int(b[::-1])

print(f'{A if A > B else B}')