# https://www.acmicpc.net/problem/2922
import sys
g = range
iStr = sys.stdin.readline().rstrip()

bList = [idx for idx in g(len(iStr)) if iStr[idx] == '_']
JA, MO = 0, 1
jmList = [[JA, MO][aChar in 'AEIOU'] for aChar in iStr]

ret = 0

def dfs(bIdx):
    if bIdx == len(bList):
        global ret
        bef = -1
        cnt = -1
        for idx in g(len(jmList)):
            if bef != jmList[idx]:
                cnt = 1
                bef = jmList[idx]
            else:
                cnt += 1
                if cnt >= 3:
                    return
        
        jCnt, mCnt = 0, 0
        for idx in g(len(jmList)):
            if idx not in bList: continue
            if jmList[idx] == JA:
                jCnt += 1
            else:
                mCnt += 1
        ret += 21**jCnt * 5**mCnt
        if 'L' not in iStr:
            ret -= 20**jCnt * 5**mCnt
            
        return

    cIdx = bList[bIdx]
    jmList[cIdx] = JA
    dfs(bIdx + 1)
    
    jmList[cIdx] = MO
    dfs(bIdx + 1)

if bList:
    dfs(0)
    print(ret)
else:
    print(0)