n = int(input())


def avg_up(txt):
    lst = list(map(int, txt.split()))
    scores = lst[1:]
    student_num = lst[0]
    avg = sum(scores)/student_num

    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1

    percentage = cnt / student_num * 100

    return print(f'{percentage:.3f}%')


for i in range(n):
    txt2 = input()
    avg_up(txt2)