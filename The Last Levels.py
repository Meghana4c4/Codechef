T=int(input())
for i in range(T):
    x,y,z=map(int,input().split())
    gap=0
    if x%3==0:
        gap = (x//3)-1
    else:
        gap= (x//3)
    print(x*y+gap*z)