def solve(n, k, a):
    indices = [[] for i in range(n + 1)]
    colours = [0] * n
    cur_col = 0
    max_painted = 0
    for i in range(n):
        if len(indices[a[i]]) < k:
            indices[a[i]] += [i]
            max_painted += 1

    max_painted = max_painted - (max_painted % k)
    for arr in indices:
        for x in arr:
            colours[x] = (cur_col % k) + 1
            cur_col += 1
            if cur_col >= max_painted:
                print(*colours); return
    print(*colours)


for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, k, a)

