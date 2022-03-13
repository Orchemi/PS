import sys
input = sys.stdin.readline

N = int(input())
arr = []
for k in range(1, N+1):
    age, name = input().split()
    arr.append([int(age), name, k])

arr.sort(key=lambda x:(x[0],x[2],x[1]))

for person in arr:
    person.pop()
    print(*person)