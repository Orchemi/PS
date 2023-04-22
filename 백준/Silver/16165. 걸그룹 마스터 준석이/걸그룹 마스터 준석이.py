def main():
    def find_groups ():
        G_group = {}
        G_member = {}
        for _ in range(G):
            group_name = input()
            N = int(input())
            group = sorted([input() for _ in range(N)])
            G_group[group_name] = group
            for name in group:
                G_member[name] = group_name

        return G_group, G_member


    G, M = map(int, input().split())
    G_group, G_memeber = find_groups()
    for _ in range(M):
        name = input()
        type = int(input())

        if type:
            print(G_memeber[name])
        else:
            print(*G_group[name], sep='\n')

main()