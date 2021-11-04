import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

mToDList = [0]*13
for month in g(2, 13):
    if month == 3:
        mToDList[month] = mToDList[month-1] + 28
    else:
        mToDList[month] = mToDList[month-1] + 30
        if (month <= 8 and month % 2 == 0) or (month > 8 and month % 2):
            mToDList[month] += 1

def monthToDay(sMonth, sDay, eMonth, eDay):
    return mToDList[sMonth] + sDay, mToDList[eMonth] + eDay

n = ifunc()[0]
bo = [monthToDay(*ifunc()) for _ in g(n)]

bo = sorted(bo)
    
ret = 0

limit = mToDList[3]+1
endLimit = mToDList[11]+30
bIdx = 0
while True:
    ret += 1
    maxCover = -1
    for aIdx in g(bIdx, len(bo)):
        s, e = bo[aIdx]
        if s <= limit:
            if maxCover < e:
                maxCover = e
        else:
            bIdx = aIdx
            break
    else:
        if maxCover <= endLimit:
            ret = 0
        break

    if maxCover == -1:
        ret = 0
        break

    limit = maxCover
    if limit > endLimit:
        break

print(ret)