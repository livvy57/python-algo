cnt = int(input())
l = []
for _ in range(cnt):
    l.append(int(input()))

l = list(set(l))
l.sort()
[print(i) for i in l]