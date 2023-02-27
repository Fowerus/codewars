# [Retired]Dubstep
def song_decoder(song):
    return ' '.join(song.replace('WUB', '').split())

# [Retired]Double Cola
def who_is_next(names, r):
    s = 0
    for i in range(0,(r//2)+1):
        d = 0
        for _ in range(1,len(names)+1):
            d += 2**i
            if s +d >= r:
                d /= 2**i
                if d == len(names):
                    return names[len(names)-1]
                return names[int(d-1)]
        s += d
