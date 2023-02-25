n, k = map(int, input().split())
g = list(map(int, input().split()))

g.sort(reverse=True)
print(g[k-1])
