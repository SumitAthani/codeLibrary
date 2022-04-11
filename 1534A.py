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
m1 = []
m2 = []
s = ""
for i in range(50):
    for j in range(50):
        if j % 2 == 1:
            if i % 2:
                s += "R"
            else:
                s += "W"
        else:
            if i % 2:
                s += "W"
            else:
                s += "R"
    m1.append(s)
    s = ""
s = ""
for i in range(50):
    for j in range(50):
        if j % 2 == 0:
            if i % 2:
                s += "R"
            else:
                s += "W"
        else:
            if i % 2:
                s += "W"
            else:
                s += "R"
    m2.append(s)
    s = ""

# print(m1, m2)
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list()
    for i in range(n):
        a.append(input())
    f1 = 0
    f2 = 0

    # print(m1, m2)
    # print(a)
    for i in range(n):
        for j in range(m):
            if a[i][j] == ".":
                continue
            else:
                if a[i][j] != m1[i][j]:
                    f1 = 1
                    break
    for i in range(n):
        for j in range(m):
            if a[i][j] == ".":
                continue
            else:
                if a[i][j] != m2[i][j]:
                    f2 = 1
                    break
    # print(m1[0][0])
    # print(f1, f2)
    if f1 == 1 and f2 == 1:
        print("NO")
    else:
        print("YES")
        if not f1:
            for i in range(n):
                for j in range(m):
                    print(m1[i][j], end="")
                print()
        else:
            for i in range(n):
                for j in range(m):
                    print(m2[i][j], end="")
                print()