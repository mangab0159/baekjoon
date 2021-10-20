import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
iList = ifunc()
m = ifunc()[0]

dp = [[-1]*3 for _ in g(n)]

pSum = [0]
aSum = 0
for item in iList:
    aSum += item
    pSum.append(aSum)

for idx in g(n-1, -1, -1):
    for cnt in g(3):
        aVal = -1
        bVal = -1

        if idx+m >= n or cnt-1 < 0:
            aVal = 0
        else:
            aVal = dp[idx+m][cnt-1]

        if idx+1 >= n:
            bVal = 0
        else:
            bVal = dp[idx+1][cnt]

        end = min(idx+m, n)
        dp[idx][cnt] = max(aVal + pSum[end] - pSum[idx], bVal)

print(dp[0][2])
