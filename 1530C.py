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
    n = int(input())
    val = n - (n//4)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # print(a[-val::])
    a.sort()
    b.sort()
    x = sum(a[-val::])
    y = sum(b[-val::])
    if x >= y:
        print(0)
    else:
        c = 0
        for i in range(1, n+1):
            valch = n+i - ((n+i)//4)
            # print("HBDJCSBDJCBDSBSDCKDSNKCLNDNKSDC", valch)
            a.append(100)
            # b.insert(0, 0)
            c += 1
            if sum(a[-valch::]) >= sum(b[-valch::]):
                break

        print(c)