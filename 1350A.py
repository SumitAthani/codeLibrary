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


def smallestDivisor(n):
    # if divisible by 2
    if (n % 2 == 0):
        return 2;

    # iterate from 3 to sqrt(n)
    i = 3;
    while (i * i <= n):
        if (n % i == 0):
            return i;
        i += 2;

    return n;


for _ in range(int(input())):
    n, k = map(int, input().split())
    z = 0
    for i in range(k):
        if n % 2 != 0:
            n += smallestDivisor(n)
        else:
            z = k - i
            break
    print(n + z * 2)