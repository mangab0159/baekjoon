# https://www.acmicpc.net/problem/2758
import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n = 0
def dfs(depth, k, m, dp):
    global n
    if depth == n-1:
        dp[depth][k] = 1
        return dp[depth][k] 
    
    if dp[depth][k] != -1:
        return dp[depth][k]

    dp[depth][k] = 0
    for ck in g(2*k, m//(2**(n-1-(depth+1)))+1):
        dp[depth][k] += dfs(depth+1, ck, m, dp)
    
    return dp[depth][k]

t = ifunc()[0]
while t:
    t -=1
    n, m = ifunc()

    ret = 0
    dp = [[-1 for _ in g(m+1)] for _ in g(n)]
    for k in g(1, m//(2**(n-1))+1):
        dfs(0, k, m, dp)
        ret += dp[0][k]

    print(ret)