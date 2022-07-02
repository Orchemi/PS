import sys
input = sys.stdin.readline

def check(idx):
    global part, pl
    stack = stacks[idx]

    if len(stack) != pl: return 0

    for i in range(pl):
        if not part[i] == stack[i]: return 0
    return 1


txt = input().rstrip()
part = input().rstrip()
pl = len(part)
stacks = [[]]
ls = [0]

cur_stack_idx = 0
k = 0
for t in txt:
    if t == part[k]:
        stacks.append([t])
        cur_stack_idx += 1
        ls.append(1)

    else:
        stacks[cur_stack_idx].append(t)
        ls[cur_stack_idx] += 1

    # 현재 stack에 모인 문자가 pl과 같을 때
    if ls[cur_stack_idx] == pl:
        while check(cur_stack_idx):
            stacks.pop()
            ls.pop()
            cur_stack_idx -= 1


def is_empty(stacks):
    for stack in stacks:
        if stack: return 0
    return 1

if is_empty(stacks):
    print('FRULA')
    quit()

for stack in stacks:
    print(*stack, sep='', end='')