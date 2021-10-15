# https://www.acmicpc.net/problem/14501
import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
tList = []
pList = []
for _ in g(n):
    t, p = ifunc()
    tList.append(t)
    pList.append(p)

dp  = [-1 for _ in g(n)]

def dfs(s):
    global dp, n
    if s == n:
        return 0
    if dp[s] != -1:
        return dp[s]
    
    maxVal = -1
    for ns in g(s+tList[s], n+1):
        if ns > n: continue
        aVal = dfs(ns)
        maxVal = [maxVal, aVal][maxVal < aVal]
    dp[s] = [pList[s]+maxVal, 0][maxVal == -1]

    return dp[s]

maxVal = -1
for idx in g(n):
    aVal = dfs(idx)
    maxVal = [maxVal, aVal][maxVal < aVal]

print(maxVal)