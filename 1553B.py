# from __future__ import division, print_function

# import itertools
# import sys
# from atexit import register

# if sys.version_info[0] < 3:
#     from io import BytesIO as stream
# else:
#     from io import StringIO as stream

# if sys.version_info[0] < 3:
#     class dict(dict):
#         """dict() -> new empty dictionary"""

#         def items(self):
#             """D.items() -> a set-like object providing a view on D's items"""
#             return dict.iteritems(self)

#         def keys(self):
#             """D.keys() -> a set-like object providing a view on D's keys"""
#             return dict.iterkeys(self)

#         def values(self):
#             """D.values() -> an object providing a view on D's values"""
#             return dict.itervalues(self)

#     input = raw_input
#     range = xrange

#     filter = itertools.ifilter
#     map = itertools.imap
#     zip = itertools.izip


# def sync_with_stdio(sync=True):
#     """Set whether the standard Python streams are allowed to buffer their I/O.

#     Args:
#         sync (bool, optional): The new synchronization setting.

#     """
#     global input, flush

#     if sync:
#         flush = sys.stdout.flush
#     else:
#         sys.stdin = stream(sys.stdin.read())
#         def input(): return sys.stdin.readline().rstrip('\r\n')

#         sys.stdout = stream()
#         register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


# mod = 1000000007


# #Code From Here

for _ in range(int(input())):
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    f = 0
    for i in range(n):
        for j in range(n):
            val = m-j-1
            if i+j < val:
                continue
            l1 = i
            r = i+j
            l2 = r - val
            if s[l1:r+1]+s[l2:r][::-1]==t:
                f = 1
                break

    if f:
        print("YES")
    else:
        print("NO")