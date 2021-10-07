# https://www.acmicpc.net/problem/1244
import sys

iFunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n = iFunc()[0]
sw = iFunc()
m = iFunc()[0]

while m:
    m -= 1
    gd, sNum = iFunc()

    
    if gd == 1:
        for idx in g(sNum-1, n, sNum):
            sw[idx] ^= 1
    else:
        sNum -= 1
        aCnt = 0
        while sNum+aCnt < n and sNum-aCnt >= 0:
            if sw[sNum+aCnt] != sw[sNum-aCnt]:
                break
            aCnt += 1

        for idx in g(sNum-aCnt+1, sNum+aCnt):
            sw[idx] ^= 1

for idx in g(0, n, 20):
    aNum = min(n-idx, 20)
    print(*sw[idx:idx+aNum])

