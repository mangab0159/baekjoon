import sys 
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, m = ifunc()

aSet = set()
for _ in g(n):
    name = sys.stdin.readline().rstrip()
    aSet.add(name)

names = []
for _ in g(m):
    name = sys.stdin.readline().rstrip()
    if name in aSet:
        names.append(name)

names = sorted(names)
print(len(names))
for name in names:
    print(name)
