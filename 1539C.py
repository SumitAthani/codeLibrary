import atexit
import io
import sys

buff = io.BytesIO()
sys.stdout = buff


@atexit.register
def write():
    sys.__stdout__.write(buff.getvalue())


n, k, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
f = 0
c = 1
l = []
for i in range(n - 1):
    z = a[i + 1] - a[i]
    if z > x:
        c += 1
        val = (z + x - 1) // x - 1
        l.append(val)
l.sort()
ans = 0
# print(c)
for i in l:
    if i <= k:
        k -= i
        c -= 1
    else:
        break
# print(l)
# print(a)
print(c)