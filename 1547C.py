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
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


mod = 1000000007

for _ in range(int(input())):
    z = input()
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c1 = 0
    c2 = 0
    val = []
    f = 0
    while c1 < n or c2 < m:
        if c1 == n:
            if b[c2] <= k:
                val.append(b[c2])
                if b[c2] == 0:
                    k += 1
                c2 += 1
            else:
                f = 1
                break
        elif c2 == m:
            if a[c1] <= k:
                val.append(a[c1])
                if a[c1] == 0:
                    k += 1
                c1 += 1
            else:
                f = 1
                break
        else:
            if a[c1] <= k:
                val.append(a[c1])
                if a[c1] == 0:
                    k += 1
                c1 += 1
            elif b[c2] <= k:
                val.append(b[c2])
                if b[c2] == 0:
                    k += 1
                c2 += 1
            else:
                f = 1
                break
    if f:
        print(-1)
    else:
        print(*val)