for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    c = 0
    t = a[-1]
    for i in range(n):
        if t == m:
            break
        else:
            if a[n-i-1]>t:
                t = a[n-i-1]
                c+=1
    print(c)