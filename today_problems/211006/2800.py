import sys
g = range
iStr = sys.stdin.readline().rstrip()

opList = []
op2List = []
clDict = {}
clList = []
for idx, aChar in enumerate(iStr):
    if aChar == '(':
        opList.append(idx)
        op2List.append(idx)
    elif aChar == ')':
        clDict[op2List.pop()] = idx
for op in opList:
    clList.append(clDict[op])

ocCnt = len(opList)
cbList = []

aSet = set()

retList = []
def combi(s, depth):
    if 0 < depth <= ocCnt:
        delList = []
        for idx in cbList:
            delList += [opList[idx], clList[idx]]
        delList = sorted(delList)
        retStr = ''
        befIdx = 0
        for idx in delList:
            retStr += iStr[befIdx: idx]
            befIdx = idx + 1
        retStr += iStr[befIdx:]

        if retStr not in aSet:
            aSet.add(retStr)
            retList.append(retStr)

        if depth == ocCnt:
            return
    
    for idx in g(s, ocCnt):
        cbList.append(idx)
        combi(idx+1, depth+1)
        cbList.pop()

combi(0, 0)

retList = sorted(retList)
for ret in retList:
    print(ret)