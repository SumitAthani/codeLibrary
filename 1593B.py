import math


for _ in range(int(input())):
    a = input()
    l = len(a)
    ans = math.inf
    if int(a)%25==0:
        print(0)
        continue
    for i in range(l):
        for j in range(l):
            if i>=j:
                continue
            if (int(a[i])*10+int(a[j]))%25==0:
                ans = min(ans, l-j-1+ j-i-1)

    print(ans)