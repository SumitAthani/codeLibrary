from __future__ import division, print_function
 
import itertools
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
    n , a, b  = map(int, input().split())
    r= 0
    l = 0

    ans = []

    ans.append(a)
    for i in range(n, 0, -1):
        if i!=a and i!=b:
            ans.append(i)
    ans.append(b)

    # for i in range(1, n//2+1):
    #     if i!=a and i!=b:
    #         ans.append(i)
    if len(ans)==n and min(ans[0:n//2])==a and max(ans[n//2:n])==b:
        print(*ans)
    else:
        print(-1)