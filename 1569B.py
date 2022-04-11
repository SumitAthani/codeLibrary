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
    s = list(input())
    val = s.count("2")
    if 0<val<=2:
        print("NO")
        continue
    ans= [["=" for i in range(n)] for i in range(n)]
    c = 0
    c2 = 0
    
    for i in range(n):
        if s[i]=="2":
            c+=1
        c2=0
        f = 0
        for j in range(n):
            if i==j:
                ans[i][j] = "X"
                if s[i]=="2":
                    c2+=1
            else:
                if s[i]=="1" or s[j]=="1":
                    ans[i][j] = "="
                else:
                    c2+=1
                    if c!=val:
                        if c<c2 and f==0:
                            ans[i][j] = "+"
                            ans[j][i] = "-"
                            f = 1
                      
                    else:
                        if c2==1:
                            ans[i][j] = "+"
                            ans[j][i] = "-"
                       
            # print(*ans, sep="\n",)
            # print("c, c2", c, c2)
            # print()
        # print()
    print("YES")

    for i in ans:
        print(*i, sep="")