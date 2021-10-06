# https://www.acmicpc.net/problem/1005
import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
case = ifunc()[0]
while case:
    case -= 1
    n, k = ifunc() 
    d = [0] + ifunc()
    edges = [[] for _ in g(n+1)]

    indeg = [0 for _ in g(n+1)]
    for _ in g(k):
        x, y = ifunc()
        edges[x].append(y)
        indeg[y] += 1
    w = ifunc()[0]

    que = [v for v in g(1, n+1) if not indeg[v]]

    t = [0 for _ in g(n+1)]
    for v in que:
        t[v] += d[v]
        if v == w:
            print(t[v])
            break
        for nv in edges[v]:
            if t[nv] < t[v]:
                t[nv] = t[v]

            indeg[nv] -= 1
            if not indeg[nv]:
                que.append(nv)
    