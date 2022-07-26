for _ in range(int(input())):
    x,y,n,r=map(int,input().split())
    if n*x>r:
        print(-1)
    else:
        b=min((r-n*x)//(y-x),n)
        a=n-b
        print(a,b)

