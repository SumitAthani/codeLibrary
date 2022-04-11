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


#Code From Here

for _ in range(int(input())):
    s = list(input())
    val = s.copy()
    for i in  range(10):
        if s[i]=="?":
            if i%2:
                s[i] = "1"
            else:
                s[i] = "0"
    for i in range(10):
        if val[i]=="?":
            if i%2:
                val[i] = "0"
            else:
                val[i] = "1"
    # print(s, val)
    p1 = 0
    p2 = 0
    ans = 10
    for i in range(10):
        if i%2:
            if s[i]=="1":
                p2+=1
        if i%2==0:
            if s[i]=="1":
                p1+=1
        if (i+1)>5:
            if (i+1)%2:
                if p1>=(p2+(10-i+2)//2) or p2>=(p1+(10-i+1)//2):
                    # print(p1, p2)
                    ans = min(ans, i+1)
                    break
            else:
                if p1>=(p2+(10-i+1)//2) or p2>=(p1+(10-i+1)//2):
                    # print(p1, p2)
                    ans = min(ans, i+1)
                    break
            
            
                   
    p1 = 0
    p2 = 0
    for i in range(10):
        if i%2:
            if val[i]=="1":
                p2+=1
        if i%2==0:
            if val[i]=="1":
                p1+=1
        if (i+1)>5:
            if (i+1)%2:
                if p1>=(p2+(10-i+2)//2) or p2>=(p1+(10-i+1)//2):
                    # print(p1, p2)
                    ans = min(ans, i+1)
                    break
            else:
                if p1>=(p2+(10-i+1)//2) or p2>=(p1+(10-i+1)//2):
                    # print(p1, p2)
                    ans = min(ans, i+1)
                    break
            
            
            
    print(ans)