# https://www.acmicpc.net/problem/1535
import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
lList = ifunc()
jList = ifunc()


dp = [[0 for _ in g(101)] for _ in g(n)]
for r in g(n):
    for c in g(101):
        if r-1 < 0:
            if c-lList[r] > 0:
                dp[r][c] = jList[r]
        else:
            if c-lList[r] <= 0:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = max(dp[r-1][c-lList[r]] + jList[r], dp[r-1][c])

print(dp[n-1][100])