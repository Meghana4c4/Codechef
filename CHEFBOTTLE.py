for _ in range(int(input())):
    n,x,k=map(int,input().split())
    if n<=k:
        k=k//x
        if k<=n:
            print(k)
        else:
            print(n)
    else:
        print(k//x)
