import sys
ifunc, g = lambda:[*map(int, sys.stdin.readline().rstrip().split())], range
n, c, w = ifunc()
trees = [ifunc()[0] for _ in g(n)]
maxTree = 0
for tree in trees:
    maxTree = [maxTree, tree][maxTree < tree]

def cutTree(tree, unit):
    if tree < unit:
        return 0, 0
    cnt = tree // unit
    if tree % unit == 0:
        return cnt, (cnt-1)*c
    return cnt, cnt*c

maxScore = -50*10000*10000
for unit in g(1, maxTree+1):
    cntSum = 0
    costSum = 0
    for tree in trees:
        cnt, cost = cutTree(tree, unit)
        if cnt*w*unit <= cost: continue
        cntSum += cnt
        costSum += cost
    
    score = cntSum*w*unit - costSum
    maxScore = [maxScore, score][maxScore < score]

print([maxScore, 0][maxScore < 0])