# https://www.acmicpc.net/problem/2665
import sys
from collections import deque
ifunc, g = lambda: [*map(int, list(sys.stdin.readline().rstrip()))], range

n = int(sys.stdin.readline().rstrip())
bo = [ifunc() for _ in g(n)]
boCnt = [[3000 for _ in g(n)] for _ in g(n)]

que = deque()
boCnt[0][0] = 0
que.append((0, 0, 0))

while que:
    cr, cc, cnt = que.popleft()
    
    for nr, nc in ((cr+1, cc), (cr, cc+1), (cr-1, cc), (cr, cc-1)):
        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
        cnt2 = cnt
        if bo[nr][nc] == 0:
            cnt2 += 1
        if cnt2 < boCnt[nr][nc]:
            boCnt[nr][nc] = cnt2
            que.append((nr, nc, cnt2)) 
print(boCnt[n-1][n-1])