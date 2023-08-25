def main():
    def put_room():
        for room in rooms:
            if room['cnt'] == M: continue
            if level > room['max_level']: continue
            if level < room['min_level']: continue
            room['names'].append(name)
            room['cnt'] += 1
            return

        new_room = {
            'max_level': level+10,
            'min_level': level-10,
            'names': [name],
            'cnt': 1,
        }
        return rooms.append(new_room)

    N, M = map(int, input().split())
    rooms = []
    levels = {}
    for _ in range(N):
        level, name = input().split()
        level = int(level)
        levels[name] = level
        put_room()

    for room in rooms:
        if room['cnt'] == M:
            print('Started!')
        else:
            print('Waiting!')

        for name in sorted(room['names']):
            print(levels[name], name)

main()