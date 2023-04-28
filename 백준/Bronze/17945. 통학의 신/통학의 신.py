a, b = map(int, input().split())
k = int((a**2-b)**(1/2))
ret = {-a+k, -a-k}
print(*sorted(list(ret)))