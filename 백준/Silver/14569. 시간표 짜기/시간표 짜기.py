def main():
    N = int(input())
    clss = []
    for _ in range(N):
        n, *cls = list(input().split())
        clss.append(set(cls))

    M = int(input())
    students = []
    for _ in range(M):
        n, *student = list(input().split())
        students.append(set(student))

    for student in students:
        cnt = 0
        for cls in clss:
            if not cls - student: cnt += 1
        print(cnt)

main()