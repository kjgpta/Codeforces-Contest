for i in range(int(input())):
    n = int(input())
    s = list(input())
    st = sorted(s)
    k = 0
    for j in range(n):
        if s[j] != st[j]:
            k += 1
    print(k)