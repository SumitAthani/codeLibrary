

for _ in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    one = a.count(1)
    z =a.count(0)
    print(one*2**z)