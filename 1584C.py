
# Code From Here
 
for _ in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    *b,  = map(int, input().split())
    a.sort()
    b.sort()
    f = 0
    for i in range(n):
        if a[i]==b[i] or b[i] == a[i]+1:
            continue
        else:
            f = 1
            break
    print("NO" if f else "YES")