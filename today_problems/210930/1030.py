# https://www.acmicpc.net/problem/1030

import sys

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
s, N, K, R1, R2, C1, C2 = ifunc()

def chkBlack(r, c):
    s2 = s
    while s2 > 0:
        s2 -= 1
        isBlackR = (N-K)//2 <= (r//(N**s2))%N < N-(N-K)//2
        isBlackC = (N-K)//2 <= (c//(N**s2))%N < N-(N-K)//2
        if isBlackR == True and isBlackC == True: return True
    return False

for r in g(R1, R2+1):
    for c in g(C1, C2+1):
        print(('0', '1')[chkBlack(r, c)], end='')
    print()