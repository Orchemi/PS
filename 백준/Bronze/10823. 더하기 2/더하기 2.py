S = ''
while True:
    try:
        s = input()
        S += s
    except:
        break

print(sum(list(map(int, S.split(',')))))