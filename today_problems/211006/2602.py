# https://www.acmicpc.net/problem/2602
import sys
ifunc, g = lambda: sys.stdin.readline().rstrip(), range

duru = ifunc()
strs = [ifunc()]
strs.append(ifunc())
lenStairs = len(strs[0])
lenDuru = len(duru)

dp = [[[-1]*lenDuru for _ in g(lenStairs)] for _ in g(2)]

def dfs(bridge, stair, duIdx):
    if duIdx == lenDuru-1:
        return 1
    if dp[bridge][stair][duIdx] != -1:
        return dp[bridge][stair][duIdx]
    ret = 0
    aChar = duru[duIdx+1]
    bridge ^= 1
    for idx in g(stair+1, lenStairs):
        if strs[bridge][idx] == aChar:
            ret += dfs(bridge, idx, duIdx+1)
    bridge ^= 1
    dp[bridge][stair][duIdx] = ret
    return ret

ret = 0
for idx in g(lenStairs):
    if strs[0][idx] == duru[0]:
        ret += dfs(0, idx, 0)
    if strs[1][idx] == duru[0]:
        ret += dfs(1, idx, 0)

print(ret)