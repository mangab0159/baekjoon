import sys
g = range
n, k = [*map(int, sys.stdin.readline().rstrip().split())]
iList = [*map(int, sys.stdin.readline().rstrip())]

st = []
for aNum in iList:
    while k and st and st[-1] < aNum:
        k -= 1
        st.pop()
    st.append(aNum)

if k:
    print(''.join(map(str, st[:-k])))
else:
    print(''.join(map(str, st)))