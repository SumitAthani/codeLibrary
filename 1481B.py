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
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        j = 0
        while j < n-1 and a[j] >= a[j+1]:
            j += 1
        ans = j
        if j == n-1:
            break
        a[j] += 1
    if ans == n-1:
        print(-1)
    else:
        print(ans+1)