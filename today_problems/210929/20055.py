# https://www.acmicpc.net/problem/20055

import sys, os

# dirname = os.path.dirname(__file__)

# inputName = os.path.join(dirname, 'input.txt')
# sys.stdin = open(inputName, 'r')

# outputName = os.path.join(dirname, 'output.txt')
# sys.stdout = open(outputName, 'w')

def input():
    return sys.stdin.readline().rstrip()

N, K = list(map(int, input().split()))
aList = list(map(int, input().split()))
robotFlg = [False for _ in range(2 * N)]

turn = 0

loadPos = 0
dropPos = N - 1
zeros = 0

while zeros < K:
    turn += 1
    
    robotFlg[dropPos] = False
    loadPos = (loadPos - 1) % (2 * N)
    dropPos = (dropPos - 1) % (2 * N)
    robotFlg[dropPos] = False

    pos = dropPos
    while True:
        nPos = pos
        pos = (pos - 1) % (2 * N)
        if nPos == loadPos:
            break

        if not (robotFlg[pos] and not robotFlg[nPos] and aList[nPos] > 0):
            continue

        robotFlg[nPos] = True
        robotFlg[pos] = False
        aList[nPos] -= 1
        if aList[nPos] == 0:
            zeros += 1
            
    

    if aList[loadPos] > 0:
        aList[loadPos] -= 1
        if aList[loadPos] == 0:
            zeros += 1

        robotFlg[loadPos] = True

print(turn)