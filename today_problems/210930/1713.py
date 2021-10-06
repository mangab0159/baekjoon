# https://www.acmicpc.net/problem/1713
import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n = ifunc()[0]
m = ifunc()[0]
iList = ifunc()

bo = []
for tm in g(m):
    id = iList[tm]
    
    idFlg = False
    for item in bo:
        if id == item[0]: 
            idFlg = True
            item[1] += 1
            break
    if idFlg:
        continue

    if len(bo) < n:
        bo.append([id, 1, tm])
        continue

    minCnt, minTm, tarIdx = 10**3+1, 10**3+1, -1
    for aIdx in g(n):
        _, aCnt, aTm = bo[aIdx]
        if aCnt < minCnt or (aCnt == minCnt and aTm < minTm):
            minCnt, minTm, tarIdx = aCnt, aTm, aIdx
    
    bo[tarIdx] = [id, 1, tm]

aList = [id for id, _, _ in bo]
aList = sorted(aList)
print(*aList)