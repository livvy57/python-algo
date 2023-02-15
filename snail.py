day, night, v = map(int, input().split())
cnt = 1
climb = 0

while v > climb:
    climb += day
    if climb >= v:
        break
    else:
        climb -= night
        cnt += 1

print(cnt)