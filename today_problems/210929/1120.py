# https://www.acmicpc.net/problem/1120
import sys, os

# dirname = os.path.dirname(__file__)
# inputFile = os.path.join(dirname, 'input.txt')
# outputFile = os.path.join(dirname, 'output.txt')

# sys.stdin = open(inputFile, 'r')
# sys.stdout = open(outputFile, 'w')

def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    aStr, bStr = input().split()
    
    lenDiff = len(bStr) - len(aStr)

    minCnt = 100
    for sIdx in range(0, lenDiff + 1):
        diffCnt = 0
        aStrExt = (' ' * sIdx + aStr).ljust(len(bStr), ' ')

        for idx in range(sIdx, sIdx + len(aStr)):
            if aStrExt[idx] != bStr[idx]:
                # print(idx)
                diffCnt += 1
        # print(bStr)
        # print(aStrExt)
        # print(diffCnt)
        if diffCnt < minCnt:
            minCnt = diffCnt
    
    print(minCnt)
