t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=x*1.07
    if y<=a:
        print("YES")
    else:
        print("NO")