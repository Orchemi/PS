A = int(input())
B = int(input())

sum_val = 0
min_val = 0
for num in range(A, B+1):      # A 이상 B 이하의 숫자 각각의 num에 대하여

    if num == 1:               # num이 1이면
        continue               # 소수가 아니므로 다음 num으로
    elif num == 2:             # num이 2이면
        sum_val += num         # 소수이므로 sum_val에 num(2) 더함
        min_val = 2            # 최소 소수는 2
        continue               # 다음 num으로

    n = 2
    while num > n:
        if num % n == 0:       # n이 num의 약수이면
            num = 0            # num을 0으로 설정
            break              # 반복 탈출
        n += 1                 # n이 num의 약수가 아니면 다음 n으로

    sum_val += num             # num이 소수이면 num 더하고 아니면 0 더함

    if min_val == 0:           # min_val이 0일 때
        min_val = num          # min_val에 num 할당, 첫 소수가 입력되고 그 뒤로 끝

if sum_val == 0:
    print(-1)
else:
    print(sum_val)
    print(min_val)