import sys
from collections import deque
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, m = ifunc()
bo = [ifunc() for _ in g(n)]

def bfs():
    visited = [[False]*m for _ in g(n)]
    cntList = [[0]*m for _ in g(n)]
    delList = []

    que = deque()

    visited[0][0] = True
    que.append((0, 0))

    while que:
        r, c = que.popleft()
        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= n or nc < 0 or nc >= m or visited[nr][nc]: continue
            if bo[nr][nc] == 1:
                cntList[nr][nc] += 1
                if cntList[nr][nc] == 2:
                    delList.append((nr, nc))
                continue
            
            visited[nr][nc] = True
            que.append((nr, nc))

    cnt = len(delList)
    while delList:
        r, c = delList.pop()
        bo[r][c] = 0
    return cnt

t = 0
while True:
    t += 1
    cnt = bfs()
    if not cnt:
        print(t-1)
        break