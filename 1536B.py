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
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


mod = 1000000007

for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    ans = ""
    f = 0
    for i in range(26):
        val = chr(ord("a") + i)
        if val not in s:
            ans = val
            break
    if ans:
        print(ans)
        continue
    for i in range(26):
        for j in range(26):
            val = chr(ord("a") + i)
            val += chr(ord("a") + j)
            if val not in s:
                ans = val
                break
        if ans:
            break
    if ans:
        print(ans)
        continue

    for i in range(26):
        for j in range(26):
            for k in range(26):
                val = chr(ord("a") + i)
                val += chr(ord("a") + j)
                val += chr(ord("a") + k)
                if val not in s:
                    ans = val
                    break
            if ans:
                break
        if ans:
            break
    print(ans)