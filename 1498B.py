from __future__ import division, print_function

import itertools
import sys
from atexit import register
import bisect
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

for _ in range(int(input())):
    n, W = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = len(a)
    val = W
    ans = 1
    while len(a):
        if val == 0:
            val = W
            ans+=1
        x = bisect.bisect_left(a, val)

        if x<l and a[x]<=val:
            val -= a[x]
            l-=1
            a.remove(a[x])
        elif x>0 and a[x-1]<=val:
            val -= a[x-1]
            l-=1
            a.remove(a[x-1])
        else:
            val = W
            ans+=1

    print(ans)