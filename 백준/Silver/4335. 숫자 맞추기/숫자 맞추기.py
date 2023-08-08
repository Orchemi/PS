def main():
    def cycle():
        D = {'H': [], 'L': []}
        while True:
            N = int(input())
            if not N: return False
            ans = input()
            if ans == 'too high':
                D['H'].append(N)
            elif ans == 'too low':
                D['L'].append(N)
            else:
                for h in D['H']:
                    if N >= h: return 'N'
                for l in D['L']:
                    if N <= l: return 'N'
                return 'Y'

    while True:
        ret = cycle()
        if not ret: return
        print('Stan may be honest' if ret == 'Y' else 'Stan is dishonest')

main()