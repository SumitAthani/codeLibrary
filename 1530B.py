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
        def input(): return sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


mod = 1000000007


# Code From Here

for _ in range(int(input())):
    h, w = map(int, input().split())
    f = 0
    if h > w:
        f = 1
        h, w = w, h
    a = [[0 for i in range(w)] for j in range(h)]

    for i in range(w):
        if i % 2:
            a[0][i] = 0
            a[-1][i] = 0
        else:
            a[0][i] = 1
            a[-1][i] = 1
    for i in range(h-2):
        if not i % 2:
            continue
        a[i+1][0] = 1
        a[i+1][-1] = 1
    if h % 2 == 0:
        a[-2][0] = 0
        a[-2][-1] = 0

    if f:
        for i in range(w):
            for j in range(h):
                print(a[j][i], end="")
            print()
    else:
        for i in a:
            print(*i, sep="")
    print()