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
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    neg = 0
    pos = 0
    f = 0
    for i in range(n):
        if a[i] != b[i]:
            if b[i] == 0:
                if a[i] > 0:
                    if neg:
                        f = 0
                    else:
                        f = 1
                        break
                if a[i] < 0:
                    if pos:
                        f = 0
                    else:
                        f = 1
                        break
            elif b[i] > 0:
                if pos:
                    f = 0
                else:
                    f = 1
                    break

            elif b[i] < 0:
                if neg:
                    f = 0
                else:
                    f = 1
                    break
            if a[i] < 0:
                neg = 1
            elif a[i] > 0:
                pos = 1
        if a[i] < 0:
            neg = 1
        elif a[i] > 0:
            pos = 1
    if f:
        print("No")
    else:
        print("Yes")