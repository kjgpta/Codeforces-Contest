def func(n):
    if n%3 == 0:
        return [int(n/3), int(n/3)]
    elif n%3 == 1:
        return [int(n/3)+1, int(n/3)]
    else:
        return [int(n/3), int(n/3)+1]
test_cases = int(input())
for i in range(test_cases):
    a,b = func(int(input()))
    print(str(a)+" "+str(b))
