arr = []
while True:
    x, y = map(int, input().split())
    [print(el) for el in arr if x == 0 and y == 0]
    arr.append(x+y)
