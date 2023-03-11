current = map(int, input().split())
chesspieces = [1, 1, 2, 2, 2, 8]

for (index, pieces) in enumerate(current):
    print(chesspieces[index] - pieces, end=" ")
