while True:
    name, age, weight = input().split()
    if name=='#': break

    ret = 'Junior'
    if int(age) > 17 or int(weight) >= 80:
        ret = 'Senior'
    print(name, ret)