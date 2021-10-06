# https://www.acmicpc.net/problem/3055
import sys

g = range
R, C = map(int, sys.stdin.readline().rstrip().split())
bo = [list(sys.stdin.readline().rstrip()) for _ in g(R)]

gque = [(p//C, p%C) for p in g(R*C) if bo[p//C][p%C] == 'S']
wque = [(p//C, p%C) for p in g(R*C) if bo[p//C][p%C] == '*']

bo[gque[0][0]][gque[0][1]] = 0

def bfs():
    global gque, wque

    while gque:
        wque2 = []
        for r, c in wque:
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                if str(bo[nr][nc]) in '*DX': continue
                if (nr, nc) in wque2: continue
                wque2.append((nr, nc))

        wque = wque2

        gque2 = []
        for r, c in gque:
            if bo[r][c] == '*': continue
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                if bo[nr][nc] == 'D':
                    return bo[r][c]+1

                if bo[nr][nc] != '.': continue
                bo[nr][nc] = bo[r][c] + 1
                gque2.append((nr, nc))
        gque = gque2

        for r, c in wque:
            bo[r][c] = '*'
    return 'KAKTUS'

print(bfs())