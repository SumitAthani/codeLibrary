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
        def input(): return sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = 0
    b = 0
    c = 0
    n = n-(k-3)
    if n % 2:
        a = 1
        b = c = (n-1)//2
        for i in range(k-3):
            print(1, end=" ")
        print(a, b, c)
    else:
        if n % 4 == 0:
            a = n//2
            b = c = n//4
            for i in range(k-3):
                print(1, end=" ")
            print(a, b, c)
        else:
            a = 2
            b = n//2 - 1
            c = n//2 - 1
            for i in range(k-3):
                print(1, end=" ")
            print(a, b, c)