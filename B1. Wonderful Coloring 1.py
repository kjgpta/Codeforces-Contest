import collections
test_cases = int(input())
for i in range(test_cases):
    a = list(input())
    freq = dict(collections.Counter(a))
    sin = 0
    non_sin = 0
    for j in freq.values():
        if j == 1:
            sin += 1
        if j != 1:
            non_sin += 1
    print(non_sin+int(sin/2))