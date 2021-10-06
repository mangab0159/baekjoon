import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

R, C, T = ifunc()
bo = [ifunc() for _ in g(R)]
upAir, downAir = [(p//C, p%C) for p in g(R*C) if bo[p//C][p%C] == -1]


def move(spos, epos, inVal):
    global bo

    outVal = bo[epos[0]][epos[1]]

    dpos = (epos[0]-spos[0], epos[1]-spos[1])
    dposSize = sum([*map(abs, dpos)])
    dpos = tuple(item//dposSize
     for item in dpos)

    spos = (spos[0]+dpos[0], spos[1]+dpos[1])
    cpos = epos
    while spos != cpos:
        bpos = (cpos[0]-dpos[0], cpos[1]-dpos[1])
        bo[cpos[0]][cpos[1]] = bo[bpos[0]][bpos[1]]
        cpos = bpos
    bo[cpos[0]][cpos[1]] = inVal

    return outVal

def moveCircle(*pList):
    global bo

    sPos = pList[0]
    outVal = 0
    for ePos in pList[1:]:
        outVal = move(sPos, ePos, outVal)
        sPos = ePos
    move(sPos, pList[0], outVal)
    
    bo[pList[0][0]][pList[0][1]] = -1
    
def diffuse():
    global bo

    bo2 = [[0 for _ in g(C)] for _ in g(R)]

    for r in g(R): 
        for c in g(C):
            if bo[r][c] in [0, -1]: continue
            amount = bo[r][c]//5
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                if bo[nr][nc] == -1: continue
                bo[r][c] -= amount
                bo2[nr][nc] += amount
            bo2[r][c] += bo[r][c]

    bo2[upAir[0]][upAir[1]] = -1
    bo2[downAir[0]][downAir[1]] = -1

    bo = bo2

t = 0
while t < T:
    t += 1

    diffuse()

    p1, p2, p3 = (upAir[0], C-1), (0, C-1), (0, 0)
    moveCircle(upAir, p1, p2, p3)
    p1, p2, p3 = (downAir[0], C-1), (R-1, C-1), (R-1, 0)
    moveCircle(downAir, p1, p2, p3)

print(sum([sum(row) for row in bo])+2)