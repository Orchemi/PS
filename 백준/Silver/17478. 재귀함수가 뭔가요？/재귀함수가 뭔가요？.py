def pre(i):
    for _ in range(i):
        print(t0, end='')

def foo(i):
    global n
    if i == n:
        for t in [t2[0], t3, t4]:
            pre(i)
            print(t)
        return

    for t in t2:
        pre(i)
        print(t)

    foo(i+1)

    pre(i)
    print(t4)


t0 = '____'
t1 = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
t2 = ['"재귀함수가 뭔가요?"', '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.', '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.', '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
t3 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
t4 = '라고 답변하였지.'

n = int(input())
print(t1)
foo(0)