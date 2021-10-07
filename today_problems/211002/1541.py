# https://www.acmicpc.net/problem/1541
import sys

def plusOp(pStr: str):
    pList = [*map(int, pStr.split('+'))]
    return sum(pList)

aStr = sys.stdin.readline().rstrip()

ret = 0
cIdx = 0
if aStr[0] != '-':
    nIdx = aStr.find('-', cIdx)
    nIdx = [nIdx, len(aStr)][nIdx == -1]
    ret += plusOp(aStr[cIdx:nIdx])
    cIdx = nIdx+1
else: cIdx = 1

while cIdx != len(aStr)+1:
    nIdx = aStr.find('-', cIdx)
    nIdx = [nIdx, len(aStr)][nIdx == -1]
    
    ret -= plusOp(aStr[cIdx:nIdx])

    cIdx = nIdx+1

print(ret)