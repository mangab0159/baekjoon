# https://www.acmicpc.net/problem/17142

import sys

ifunc, g, ret = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range, 52**52

n, m = ifunc()
bo = [ifunc() for _ in g(n)]

def combi(s, cl):
    if len(cl) == m:
        global ret
        q, v = cl, [row[:] for row in bo]
        for r, c in q:
            v[r][c] = 3

        for r, c in q:
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if not (0 <= nr < n and 0 <= nc < n) or v[nr][nc] not in (0, 2): continue

                v[nr][nc] = v[r][c]+1
                q.append((nr, nc))

        ret = [ret, min(ret, max([v[p//n][p%n] for p in g(n**2) if bo[p//n][p%n] == 0]+[3])-3)][bool(min(map(min, v)))]
        return

    for p in g(s, n**2):
        r, c = p//n, p%n
        if bo[r][c] != 2: continue

        combi(p + 1, cl + [(r, c)])
            

combi(0, [])
print([ret, -1][ret == 52**52])