T=int(input())
for i in range(T):
    n,a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c,d=0,0
    for m in l:
        if m%a==0:
            c=c+1
        elif m%b==0:
            d+=1
    if c>d:
        print("BOB")
    else:
        print("ALICE")
