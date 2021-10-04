# https://www.acmicpc.net/problem/1167

import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
edges = [None for _ in g(n+1)]
for _ in g(n):
    il = ifunc()
    v = il[0]
    edges[v] = [(il[idx], il[idx+1]) for idx in g(1, len(il)-2, 2)]
    
dist = [[0, 0] for _ in g(n+1)]

def dfs(cv, pv):
    global dist
    for nv, w in edges[cv]:
        if nv == pv: continue
        dfs(nv, cv)
        dist1 = dist[nv][0]+w
        if dist1 > dist[cv][0]:
            dist[cv][1] = dist[cv][0]
            dist[cv][0] = dist1
        elif dist1 > dist[cv][1]:
            dist[cv][1] = dist1

dfs(1, 1)

print(sum(max(dist, key=lambda x: (x[0]+x[1]))))