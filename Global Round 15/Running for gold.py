for abcd in range(int(input())):
    n=int(input())
    ans=[]
    for i in range(n):
        ai=list(map(int,input().split()))
        ans.append(ai)
    k=0
    x=0
    for j in range(n):
        y=0
        for i in range(5):
            if(ans[j][i]<ans[k][i]):
                y=y+1
        if(y>=3):
            k=j
    for j in range(n):
        y=0
        for i in range(5):
            if(ans[j][i]<ans[k][i]):
                y=y+1
        if(y>=3):
            x=1
            break
    if n==1:
        print(1)
        continue
    if(x==1):
        print(-1)
    else:
        print(k+1)