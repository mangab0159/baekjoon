import sys

ifunc, g = lambda: sys.stdin.readline().rstrip().split(), range

name = ifunc()[0]

name = sorted(name)

evenList = []
oddList = []

bItem = name[0]
aList = [bItem]
for item in name[1:]:
    if bItem == item:
        aList.append(item)
        continue
    if len(aList)%2:
        oddList.append(aList)
    else:
        evenList.append(aList[:len(aList)//2])
    aList = [item]
    bItem = item
if len(aList)%2:
    oddList.append(aList)
else:
    evenList.append(aList[:len(aList)//2])

if len(oddList) > 1:
    print("I'm Sorry Hansoo")
else:
    odd = [] if not oddList else oddList[0]
    if len(odd) > 1:
        evenList.append(odd[:-1][:len(odd)//2])
        odd = odd[-1:]

    evenList = sorted(evenList, key=lambda x: x[0])

    ret = []
    for even in evenList:
        ret += even
    ret += odd
    evenList = sorted(evenList, key=lambda x: x[0], reverse=True)
    for even in evenList:
        ret += even

    print(''.join(ret))