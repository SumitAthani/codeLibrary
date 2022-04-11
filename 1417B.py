# from __future__ import division, print_function
# import bisect
# import math
# import heapq
# import itertools
# import sys
# from collections import deque
# from atexit import register
# from collections import Counter
# from functools import reduce
#
# if sys.version_info[0] < 3:
#     from io import BytesIO as stream
# else:
#     from io import StringIO as stream
#
# if sys.version_info[0] < 3:
#     class dict(dict):
#         """dict() -> new empty dictionary"""
#
#         def items(self):
#             """D.items() -> a set-like object providing a view on D's items"""
#             return dict.iteritems(self)
#
#         def keys(self):
#             """D.keys() -> a set-like object providing a view on D's keys"""
#             return dict.iterkeys(self)
#
#         def values(self):
#             """D.values() -> an object providing a view on D's values"""
#             return dict.itervalues(self)
#
#
#     input = raw_input
#     range = xrange
#
#     filter = itertools.ifilter
#     map = itertools.imap
#     zip = itertools.izip
#
#
# def sync_with_stdio(sync=True):
#     """Set whether the standard Python streams are allowed to buffer their I/O.
#
#     Args:
#         sync (bool, optional): The new synchronization setting.
#
#     """
#     global input, flush
#
#     if sync:
#         flush = sys.stdout.flush
#     else:
#         sys.stdin = stream(sys.stdin.read())
#         input = lambda: sys.stdin.readline().rstrip('\r\n')
#
#         sys.stdout = stream()
#         register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


mod = 1000000007

for _ in range(int(input())):
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if t / 2 in d:
        z = d[t / 2]
    c = 0
    for i in a:
        if i < t / 2:
            print(0, end=" ")
        elif i > t / 2:
            print(1, end=" ")
        else:
            if c % 2 == 0:
                print(1, end=" ")
                c += 1
            else:
                print(0, end=" ")
                c += 1
    print()