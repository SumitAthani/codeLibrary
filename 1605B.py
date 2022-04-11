from __future__ import division, print_function
 
import itertools
from os import sep
import sys
from atexit import register
 
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
 
if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
 
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
 
        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
 
        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        def input(): return sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
 
 
mod = 1000000007
 
 
# Code From Here
 
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    v = sorted(s)
    if s==v:
        print(0)
    else:
        print(1)
        l = []
        r = []
        c1 = 0
        c2 = 0
        for i in range(n):
            if s[i]=="1":
                l.append(i+1)
                c1+=1
            else:
                r.append(i+1)
                c2+=1
        x = min(c1, c2)
        rem = abs(c1-c2)
        ans1 = []
        ans2 = []
        # print(l, r)
        # print("x", x)
        for i in range(x):
            if l[i]<r[c2-i-1]:
                ans1.append(l[i])
                ans2.append(r[c2-i-1])
            else:
                break
        ans2.reverse()
        ans = ans1+ans2
        print(len(ans), *ans, sep=" ")
        # print(*ans1, *ans2, sep=" ")