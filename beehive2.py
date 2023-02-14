destn = int(input())
cnt = 1
room = 1

while destn > room:
    if destn == 1:
        print(1)
        break

    room += cnt*6
    cnt += 1

print(cnt)

