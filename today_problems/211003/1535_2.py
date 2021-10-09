# https://www.acmicpc.net/problem/1535
import sys

ifunc, range = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n = ifunc()[0]
lList = ifunc()
jList = ifunc()

ret = -1

def dfs(p, joy, depth):
    if depth == n:
        global ret
        ret = [ret, joy][ret < joy]
        return
    
    p -= lList[depth]
    if p > 0:
        dfs(p, joy+jList[depth], depth+1)
    
    p += lList[depth]
    dfs(p, joy, depth+1)
        
dfs(100, 0, 0)
print(ret)