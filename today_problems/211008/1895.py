import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

r, c = ifunc()
bo = [ifunc() for _ in g(r)]
T = ifunc()[0]
bo2 = []
for cr in g(r-2):
    for cc in g(c-2):
        aList = []
        for dr in g(3):
            for dc in g(3):
                aList.append(bo[cr+dr][cc+dc])
        aList = sorted(aList)
        bo2.append(aList[4])

bo2 = sorted(bo2)
cnt = 0
for aVal in bo2:
    if aVal >= T:
        cnt += 1

print(cnt)