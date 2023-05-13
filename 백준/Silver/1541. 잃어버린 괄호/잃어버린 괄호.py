txt = input()
arr = txt.split('-')
arr = [sum([int(n) for n in a.split('+')]) for a in arr]
print(arr[0]-sum(arr[1:]))