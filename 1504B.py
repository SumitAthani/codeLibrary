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
from typing import List

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
    n = int(input())
    a = list(input())
    b = list(input())
    if sorted(a) != sorted(b):
        print("NO")
        continue
    back = -1
    bal = 0
    inv = 0
    flag = 0
    for i in range(n):
        if a[i] == "1":
            bal += 1
        else:
            bal -= 1
        if a[i] != b[i]:
            inv += 1
        if bal == 0:
            if inv == 0 or inv == (i-back):
                pass
            else:
                flag = 1
            back = i
            inv = 0

    if inv == 0 or inv == (n-back):
        pass
    else:
        flag = 1
    # print(a)
    if flag:
        print("NO")
    else:
        print("YES")