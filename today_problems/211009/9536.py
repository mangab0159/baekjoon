import sys
ifunc, g = lambda: sys.stdin.readline().rstrip().split(), range

t = int(ifunc()[0])
while t:
    t -= 1
    records = ifunc()
    sounds = set()
    while True:
        iList = ifunc()
        if iList[1] == 'does': break
        sounds.add(iList[2])
    fox = []
    for sound in records:
        if sound in sounds: continue
        fox.append(sound)
    
    print(' '.join(fox))
