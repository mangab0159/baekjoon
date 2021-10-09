# https://www.acmicpc.net/problem/1302
from collections import defaultdict
import sys
g = range
n = int(sys.stdin.readline().rstrip())

aDict = defaultdict(int)

for _ in g(n):
    iStr = sys.stdin.readline().rstrip()
    aDict[iStr] += 1

maxKeyList = []
maxKey = ''
maxNum = -1
for key, val in aDict.items():
    if val > maxNum:
        maxNum = val
        maxKey = key
        maxKeyList = [key]
    elif val == maxNum:
        maxKeyList.append(key)
maxKeyList = sorted(maxKeyList)
print(maxKeyList[0])