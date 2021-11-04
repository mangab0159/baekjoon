import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
wList = ifunc()
maxVal = 0
def dfs(wList, score):
    if len(wList) == 3:
        global maxVal
        score += wList[0] * wList[2]
        if maxVal < score:
            maxVal = score
        return

    for idx in g(1, len(wList)-1):
        w2List = []
        for idx2 in g(len(wList)):
            if idx != idx2:
                w2List.append(wList[idx2])
        
        dfs(w2List, score + wList[idx-1] * wList[idx+1])

dfs(wList, 0)
print(maxVal)