ifun, g, ret = lambda: [*map(int, input().rstrip().split())], range, -1

vNum = ifun()[0]
edges = [None for _ in g(vNum + 1)]
for _ in g(vNum):
    iL = ifun()
    edges[iL[0]] = [(iL[ix], iL[ix+1]) for ix in g(1, len(iL) - 1, 2)]

# 제일 먼 정점 찾는 함수
# (현재 정점, 이전 정점) -> [제일 먼 정점, 제일 먼 정점까지 거리]
def dfs(cv, pv):
    vt, vtDist = cv, 0
    for nv, w in edges[cv]:
        if nv == pv: continue
        vt1, vt1Dist = dfs(nv, cv)
        vt1Dist += w
        vt, vtDist = [(vt, vtDist), (vt1, vt1Dist)][vtDist < vt1Dist]
        
    return (vt, vtDist)

vt, _ = dfs(1, 1)
_, ret = dfs(vt, vt)
print(ret)

