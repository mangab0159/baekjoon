# https://www.acmicpc.net/problem/1455
import sys

ifunc, g = lambda: [*map(int, list(sys.stdin.readline().rstrip()))], range

n, m = [*map(int, sys.stdin.readline().rstrip().split())]
bo = [ifunc() for _ in g(n)]

def flip(a, b):
    for r in g(a+1):
        for c in g(b+1):
            bo[r][c] ^= 1

cnt = 0
for r in g(n-1, -1, -1):
    for c in g(m-1, -1, -1):
        if bo[r][c] == 1:
            cnt += 1
            flip(r, c)
print(cnt)