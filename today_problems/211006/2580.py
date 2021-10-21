import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

bo = [ifunc() for _ in g(9)]
zeros = []
for r in g(9):
    for c in g(9):
        if bo[r][c] == 0:
            zeros.append((r, c))

def dfs(depth):
    if depth == len(zeros):
        return True

    r, c = zeros[depth]
    br, bc = (r//3)*3, (c//3)*3

    flgList = [False] * 10
    for idx in g(9):
        aNum = bo[r][idx]
        bNum = bo[idx][c]
        dr, dc = idx//3, idx%3
        cNum = bo[br+dr][bc+dc]

        flgList[aNum] = True
        flgList[bNum] = True
        flgList[cNum] = True
    
    for pNum in g(1, 10):
        if flgList[pNum]: continue
        bo[r][c] = pNum
        if dfs(depth+1):
            return True
        bo[r][c] = 0

    return False

dfs(0)
for row in bo:
    print(*row)