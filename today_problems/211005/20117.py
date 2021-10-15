# https://www.acmicpc.net/problem/20117
import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
aList = ifunc()

aList = sorted(aList)

if len(aList)%2:
    print(2*sum(aList[len(aList)//2+1:])+aList[len(aList)//2])
else:
    print(2*sum(aList[len(aList)//2:]))
