import sys
from typing import IO
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, m = ifunc()
bo = [ifunc() for _ in g(n)]

def melt(q):
    global bo

    bo2 = []
    for row in bo:
        bo2.append(row[:])

    nxtQ = []
    for r, c in q:
        zCnt = 0
        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if bo[nr][nc] == 0:
                zCnt += 1
        bo2[r][c] = max(bo[r][c] - zCnt, 0)
        if bo2[r][c]:
            nxtQ.append((r, c))

    bo = bo2
    return nxtQ

def bfs(iPos):
    iceCnt = 0

    q = []
    visited = [[False]*m for _ in g(n)]

    iceCnt += 1
    visited[iPos[0]][iPos[1]] = True
    q.append(iPos)
    for r, c in q:
        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if visited[nr][nc]: continue
            if bo[nr][nc] == 0: continue

            iceCnt += 1
            visited[nr][nc] = True
            q.append((nr, nc))

    return iceCnt


q = []
for r in g(n):
    for c in g(m):
        if bo[r][c]:
            q.append((r, c))

t = 0
while True:
    t += 1
    q = melt(q)

    if q:
        iceCnt = bfs(q[0])
        if iceCnt != len(q):
            break
    else:
        t = 0
        break
print(t)
