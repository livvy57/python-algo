a, b, c = map(int, input().split())
i = 0

while True:
    prod = a + b*i
    extra = c*i
    if extra > prod:
        print(i)
        break
    if b > c:
        print(-1)
        break
    i += 1
