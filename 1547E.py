from __future__ import division, print_function

import itertools
import math
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
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


mod = 1000000007

for _ in range(int(input())):
    z = input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    # ans = [math.inf for i in range(n)]
    ans = [math.inf] * n
    # val = [math.inf] * n
    for i in range(k):
        ans[a[i] - 1] = t[i]
    val = ans.copy()
    c1 = 0
    c2 = 0
    fl = math.inf
    fr = math.inf
    # print(*ans)

    for i in range(n):
        fl = min(fl + 1, ans[i])
        ans[i] = fl

    for i in range(n - 1, -1, -1):
        fr = min(fr + 1, ans[i])
        ans[i] = fr
    print(*ans)