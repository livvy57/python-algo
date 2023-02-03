alpha = list(input())

def dials():
    clock = []
    for x in alpha:
        if x in {"A", "B", "C"}:
            num = 2
        elif x in {"D", "E", "F"}:
            num = 3
        elif x in {"G", "H", "I"}:
            num = 4
        elif x in {"J", "K", "L"}:
            num = 5
        elif x in {"M", "N", "O"}:
            num = 6
        elif x in {"P", "Q", "R", "S"}:
            num = 7
        elif x in {"T", "U", "V"}:
            num = 8
        elif x in {"W", "X", "Y", "Z"}:
            num = 9
        clock.append(num)
    return clock

clock = dials()
time = 0
for a in range(len(clock)):
     time += clock[a-1] + 1
print(time)

