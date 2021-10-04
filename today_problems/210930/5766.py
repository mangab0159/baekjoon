# https://www.acmicpc.net/problem/5766

import sys
from collections import Counter

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

while True:
    n, m = ifunc()
    if n == 0 and m == 0: break

    il = []
    for _ in g(n):
        il += ifunc()

    c = Counter(il).most_common()
    alist = [id for id, cnt in c if cnt == c[1][1]]
    alist = sorted(alist)
    print(*alist)