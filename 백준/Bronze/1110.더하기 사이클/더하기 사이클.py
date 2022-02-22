num = int(input())
cnt = 0
target = num

while True:
    tens = target // 10
    ones = target % 10

    num1d = tens + ones
    result = int(str(ones) + str(num1d)[-1])
    cnt += 1

    if result == num:
        print(cnt)
        break
    else:
        target = result