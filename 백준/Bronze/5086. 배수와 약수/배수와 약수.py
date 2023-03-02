def main():
    n, m = map(int, input().split())
    if n+m == 0: return False
    if not n%m: return 'multiple'
    if not m%n: return 'factor'
    return 'neither'

while True:
    ret = main()
    if not ret: break
    print(ret)