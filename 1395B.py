from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce

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

n, m, x, y = map(int, input().split())
h = y
v = x
print(x, y)
for i in range(y + 1, m + 1):
    print(x, i)
for i in range(y - 1, 0, -1):
    print(x, i)
c = 1
v = x
for i in range(n - x):
    v += 1
    if c % 2 != 0:
        for j in range(1, m + 1):
            print(v, j)
        c += 1
    else:
        for j in range(m, 0, -1):
            print(v, j)
        c += 1
if (n - x) % 2 == 0:
    for i in range(1, x):
        if c % 2 != 0:
            for j in range(1, m + 1):
                print(i, j)
            c += 1
        else:
            for j in range(m, 0, -1):
                print(i, j)
            c += 1

else:
    c = 1
    for i in range(1, x):
        if c % 2 == 0:
            for j in range(1, m + 1):
                print(i, j)
            c += 1
        else:
            for j in range(m, 0, -1):
                print(i, j)
            c += 1