# https://www.acmicpc.net/problem/1600
import sys
from collections import deque
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

k = ifunc()[0]
w, h = ifunc()
boOrig = [ifunc() for _ in g(h)]

bo = [[row[:] for row in boOrig] for _ in g(k+1)]

que = deque()
bo[0][0][0] = 2
que.append((0, 0, 0))

def getNPs(r, c):
    return (((r+1, c), (r, c+1), (r-1, c), (r, c-1)), ((r+2, c+1), (r+1, c+2), (r-2, c+1), (r-1, c+2), \
        (r-2, c-1), (r-1, c-2), (r+1, c-2), (r+2, c-1)))

while que:
    r, c, kCnt = que.popleft()
    aCnt = bo[kCnt][r][c]
    for isHorse, nps in enumerate(getNPs(r,c)):
        for nr, nc in nps:
            if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
            if kCnt+isHorse > k: continue
            cmpCnt = bo[kCnt+isHorse][nr][nc]
            if cmpCnt == 1 or (cmpCnt != 0 and cmpCnt <= aCnt+1): continue

            bo[kCnt+isHorse][nr][nc] = aCnt+1
            que.append((nr, nc, kCnt+isHorse))

ret = min([bo[kCnt][h-1][w-1] for kCnt in g(k+1) if bo[kCnt][h-1][w-1] != 0] + [500*500])
print([ret-2, -1][ret == 500*500])