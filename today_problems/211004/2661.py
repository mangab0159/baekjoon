# https://www.acmicpc.net/problem/2661
import sys

g = range
n = int(sys.stdin.readline().rstrip())

tar = ''

def dfs(depth):
    global tar
    if depth == n:
        print(tar)
        return True


    for aNum in '123':
        tar += aNum

        for aCnt in g(1, len(tar)//2+1):
            if tar[-2*aCnt:-aCnt] == tar[-aCnt:]:
                break
        else:
            if dfs(depth+1):
                return True

        tar = tar[:-1]
    
    return False

dfs(0)