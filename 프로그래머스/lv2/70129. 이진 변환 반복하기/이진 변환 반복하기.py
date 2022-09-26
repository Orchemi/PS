def solution(s):
    D = {'0': 0, '1': 0}
    cnt = 0
    while s != '1':
        cnt += 1
        new_s, add_0 = main(s)
        s = new_s
        D['0'] += add_0
        
    answer = [cnt, D['0']]
    return answer


def main(s):
    D = {'0': 0, '1': 0}
    for c in s:
        D[c] += 1
    
    one = D['1']
    st = ''
    while one > 0:
        st = str(one%2)+st
        one = one//2
    return st, D['0']
    