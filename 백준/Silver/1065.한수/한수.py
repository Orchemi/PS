def hansoo(num):
    if num <= 99:
        return num
    else:

        cnt = 0
        for n in range(100, num+1):
            a3 = n // 100
            a2 = (n % 100) // 10
            a1 = (n % 100) % 10

            if a1 + a3 == 2 * a2:
                cnt += 1

        return cnt + 99


num = int(input())
print(hansoo(num))