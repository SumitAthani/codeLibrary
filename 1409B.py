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

for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    ans1 = 0
    ans2 = 0
    a1 = a
    b1 = b
    n1 = n
    c = a - x
    d = b - y

    if c >= n:
        a = a - n
        n = 0
    else:
        a = x
        n -= c
        if d >= n:
            b -= n
            n = 0
        else:
            b = y
            n -= d
    ans1 = a * b
    if d >= n1:
        b1 = b1 - n1
        n1 = 0
    else:
        b1 = y
        n1 -= d
        if c >= n1:
            a1 -= n1
            n1 = 0
        else:
            a1 = x
            n1 -= c
    ans2 = a1 * b1
    # print(a, b, a1, b1)
    print(min(ans1, ans2))