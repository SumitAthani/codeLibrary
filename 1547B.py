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
    s = input()
    d = {}
    l = len(s)
    f = 0
    for i in s:
        if ord(i) > l + 97 or (i in d):
            f = 1
            break
        else:
            d[i] = 1
    if f or "a" not in s:
        print("NO")
        continue
    right = 1
    left = 1
    val = s.index("a")
    for i in range(1, l):
        # if l == 1:
        #     break
        z = chr(97 + i)
        if z not in s:
            # print("HERE")
            f = 1
            break
        else:
            x = s.index(z)
            if x < val:
                if val - x > left:
                    f = 1
                    break
                else:
                    left += 1
            if x > val:
                if x - val > right:
                    f = 1
                    break
                else:
                    right += 1
    if f:
        print("No")
    else:
        print("YES")