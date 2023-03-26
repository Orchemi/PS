def main():
    def find_root():
        for n in range(N):
            if arr[n]==-1: return n

    def find_children(p):
        if p == remove_node: return 0
        ssum = 0
        found_remove_node = False
        for c in children[p]:
            if c == remove_node:
                found_remove_node = True
                continue
            ssum += find_children(c) if children[c] else 1

        if found_remove_node and ssum==0: return 1
        return ssum

    N = int(input())
    children = [[] for _ in range(N+1)]
    arr = list(map(int, input().split()))
    remove_node = int(input())

    for n in range(N):
        children[arr[n]].append(n)

    root = find_root()
    return find_children(root)

print(main())