# https://www.acmicpc.net/problem/1758

import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
il = [ifunc()[0] for _ in g(n)]

ret = 0
il = sorted(il, reverse=True)
for idx, val in enumerate(il):
    if val-idx < 0: continue
    ret += val-idx

print(ret)