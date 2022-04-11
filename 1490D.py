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
global d


def fun(a, val):
    if len(a) == 0:
        return

    m = max(a)
    d[m] = val

    ind = -1

    for i in range(len(a)):
        if a[i] == m:
            ind = i
            break

    fun(a[:ind], val+1)     # left search take // 0th index to ind val (max val)
    # come back and right search // from right of max val to end
    fun(a[ind+1:], val+1)

    # above are recursive call


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0 for i in range(n+1)]
    fun(a, 0)
    print(*d)