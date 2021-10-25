import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()
iList = ifunc()
iList = sorted(iList)

ret = [-1, -1, -1]
minMinDiff = 10**10
for idx in g(len(iList)-2):
    tar = -iList[idx]
    le = idx+1
    ri = len(iList)-1

    tarLe, tarRi = -1, -1
    minDiff = 10**10
    
    while le < ri:
        aSum = iList[le] + iList[ri]

        if abs(aSum-tar) < minDiff:
            minDiff = abs(aSum-tar)
            tarLe, tarRi = le, ri
            
        if aSum < tar:
            le += 1
        elif tar < aSum:
            ri -= 1
        else:
            break
    
    if minDiff == 0:
        ret = [iList[idx], iList[tarLe], iList[tarRi]]
        break
    if minDiff < minMinDiff:
        ret = [iList[idx], iList[tarLe], iList[tarRi]]
        minMinDiff = minDiff
ret = sorted(ret)
print(*ret)    