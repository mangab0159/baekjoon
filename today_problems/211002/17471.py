# https://www.acmicpc.net/problem/17471
import sys
from typing import List

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
pop = ifunc()
popSUm = sum(pop)
edges = [ifunc()[1:] for _ in g(n)]
for row in edges:
    for idx in g(len(row)):
        row[idx] -= 1
minDiff = 10**4

def chkUnion(uList: List):
    uCnt = 0
    vstd = [False for _ in g(n)]
    que = []

    sv = uList[0]
    uCnt += 1
    vstd[sv] = True
    que.append(sv)

    for cv in que:
        for nv in edges[cv]:
            if nv not in uList: continue
            if vstd[nv]: continue

            uCnt += 1
            vstd[nv] = True
            que.append(nv)

    return uCnt == len(uList)

def combi(s, cl: List):
    if 0 < len(cl) <= n//2:
        global minDiff
        cl2 = [id for id in g(n) if id not in cl]

        # print('#'*30)
        # print(cl)
        # print(cl2)

        if chkUnion(cl) and chkUnion(cl2):
            # print('possible')
            aSum = sum([pop[id] for id in cl])
            diff = abs(aSum-(popSUm-aSum))
            # print(aSum, popSUm-aSum, diff)
            minDiff = [minDiff, diff][diff < minDiff]
        # else:
            # print('impossible')

        if len(cl) == n//2:
            return

    for i in g(s, n):
        cl.append(i)
        combi(i+1, cl)
        cl.pop()


combi(0, [])

print([minDiff, -1][minDiff == 10**4])