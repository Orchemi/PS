def self_number(number):

    def self_number(num):
        total2 = 0

        for i in str(num):
            total2 += int(i)

        return num + total2

    target = list(range(1, number + 1))

    for i in range(1, number+1):
        try:
            target.remove(self_number(i))
        except ValueError:
            continue

    return '\n'.join(map(str, target))


print(self_number(10000))
