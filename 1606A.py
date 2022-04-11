for _ in range(int(input())):
    s = list(input())
    if s[0]!=s[-1]:
        s[0] = s[-1]
        print(*s, sep="")
    else:
        print(*s, sep="")