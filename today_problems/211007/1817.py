import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, m = ifunc()
wList = ifunc()

bCnt = 0
remain = 0
for w in wList:
    if remain < w:
        bCnt += 1
        remain = m-w
    else:
        remain -= w
print(bCnt)