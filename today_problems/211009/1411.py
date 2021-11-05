# 13:40
# 50*50*100*100 = 2500*10000 = 2.5 * 1000000

import sys
ifunc, g = lambda: sys.stdin.readline().rstrip(), range
n = int(ifunc())
words = [ifunc() for _ in g(n)]

def isShom(word, word2):
    charSet = set()
    visited = [False]*len(word)
    for idx, aChar in enumerate(word):
        if visited[idx]: continue
        if word2[idx] in charSet: break
        visited[idx] = True
        charSet.add(word2[idx])
        isValid = True
        indexes = []
        for idx2 in g(idx+1, len(word)):
            if word[idx2] != aChar: continue
            if word2[idx2] != word2[idx]:
                isValid = False
                break
            indexes.append(idx2)
        else:
            for index in indexes:
                visited[index] = True
        if not isValid:
            break
    else:
        return True
    return False

cnt = 0
cnt2 = 0
for idx, word in enumerate(words):
    for idx2 in g(idx+1, len(words)):
        cnt2 += 1
        word2 = words[idx2]
        if isShom(word, word2):
            cnt += 1
print(cnt)