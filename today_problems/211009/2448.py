# 15:00, 15:11, 15:46
import sys
g = range
n = int(sys.stdin.readline().rstrip())
colLen = (n//3)*5 + n//3 - 1
bo = [[' ' for _ in g(colLen)] for _ in g(n)]

def draw(len, le, ri):
    if len == 3:
        len = 5
        r, c = le
        for _ in g(3):
            for cc in g(c, c+len):
                bo[r][cc] = '*'
            if len == 3:
                bo[r][c+1] = ' '
            r -= 1
            c += 1
            len -= 2
        return
            
    nxtLen = len // 2
    midCol = (le[1]+ri[1])//2
    topRow = le[0]-nxtLen
    # top triangle
    draw(nxtLen, (topRow, (le[1] + midCol-1)//2 + 1), (topRow, (midCol+1 + ri[1])//2 - 1))
    # left triangle
    draw(nxtLen, le, (ri[0], midCol-1))
    # right triangle
    draw(nxtLen, (le[0], midCol+1), ri)

draw(n, (n-1, 0), (n-1, colLen-1))
for row in bo:
    print(''.join(row))