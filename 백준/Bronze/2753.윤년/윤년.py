yr = int(input())


if (yr % 4 == 0) and (yr % 100 != 0):
    print(1)
elif yr % 400 == 0:
    print(1)
else:
    print(0)