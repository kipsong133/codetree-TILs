def lcm(n,m):
    v = 0
    for i in range(1,min(n,m)+1):
        if n%i == 0 and m%i == 0:
            v = i
    print(n*m//v)


n,m = map(int,input().split())
lcm(n,m)