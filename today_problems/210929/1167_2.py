# https://www.acmicpc.net/problem/1167
import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n = ifunc()[0]
edges = [None for _ in g(n+1)]
for _ in g(n):
    il = ifunc()
    edges[il[0]] = [(il[idx], il[idx+1]) for idx in g(1, len(il)-2, 2)]

def dfs(root):
    dist = [-1 for _ in g(n+1)]

    st = [root]
    dist[root] = 0
    while st:
        top = st.pop()
        for nxt, w in edges[top]:
            if dist[nxt] != -1: continue
            dist[nxt] = dist[top] + w
            st.append(nxt)

    maxv, maxDist = dist.index(max(dist)), max(dist)
    return maxv, maxDist

v1, _ = dfs(1)
v2, ret = dfs(v1)

print(ret)