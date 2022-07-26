for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if n<=abs(m-k):
        print("YES")
    else:
        print("NO")
