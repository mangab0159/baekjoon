# https://www.acmicpc.net/problem/16927
import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

N, M, r = ifunc()
bo = [ifunc() for _ in g(N)]

def move(sp, ep, inVal):
    dp = (ep[0]-sp[0], ep[1]-sp[1])
    dpsz = sum([*map(abs, dp)])
    dp = (dp[0]//dpsz, dp[1]//dpsz)
    
    outVal = bo[ep[0]][ep[1]]

    sp = (sp[0]+dp[0], sp[1]+dp[1])
    cp = ep
    while cp != sp:
        bp = (cp[0]-dp[0], cp[1]-dp[1])
        bo[cp[0]][cp[1]] = bo[bp[0]][bp[1]]

        cp = bp
    bo[sp[0]][sp[1]] = inVal

    return outVal

def rotate(*pList):
    bp = pList[3]
    outVal = bo[bp[0]][bp[1]]
    for p in pList:
        outVal = move(bp, p, outVal)
        bp = p

lNum = min(N, M) // 2

p1, p2, p3, p4 = (0, 0), (N-1, 0), (N-1, M-1), (0, M-1)
n, m = N, M
for _ in g(lNum):
    r1 = r % (2*(n-1 + m-1))
    n, m = n-2, m-2

    for _ in g(r1):
        rotate(p1, p2, p3, p4)

    p1 = (p1[0]+1, p1[1]+1)
    p2 = (p2[0]-1, p2[1]+1)
    p3 = (p3[0]-1, p3[1]-1)
    p4 = (p4[0]+1, p4[1]-1)

for row in bo:
    for item in row:
        print('%d' % item, end=' ')
    print()