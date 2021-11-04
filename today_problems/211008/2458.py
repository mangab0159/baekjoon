import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, m = ifunc()
edges1 = [[] for _ in g(n+1)]
edges2 = [[] for _ in g(n+1)]

for _ in g(m):
    u, v = ifunc()
    edges1[u].append(v)
    edges2[v].append(u)

def dfs(cur, edges, visited):
    ret = 0
    for nxt in edges[cur]:
        if visited[nxt]: continue
        visited[nxt] = True
        ret += 1
        ret += dfs(nxt, edges, visited)
    
    return ret

cnt = 0
for idx in g(1, n+1):
    visited = [False]*(n+1)
    visited[idx] = True
    aNum = dfs(idx, edges1, visited)
    visited = [False]*(n+1)
    visited[idx] = True
    bNum = dfs(idx, edges2, visited)
    if aNum + bNum == n-1:
        cnt += 1
print(cnt)